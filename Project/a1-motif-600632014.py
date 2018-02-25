import sys,os

# Function definition is here
def score(s,DNA,l):
    iSeq=0
    DNACut=[]
    MaxChar=['A']*l
    MaxCharVal=[0]*l
    for iS in range(0,len(s)):
        DNACut.append(list(DNA[iSeq][(s[iS]):((s[iS])+l)]))
        iSeq += 1
    #-- cal score
    for j in range(0,l):
        cA = 0
        cT = 0
        cG = 0
        cC = 0
        for k in range(0,len(DNACut)):
            #-- count char
            if (DNACut[k][j] == 'A'):
                cA += 1
                if (cA > MaxCharVal[j]):
                    MaxCharVal[j] = cA
                    MaxChar[j] = 'A'
            elif (DNACut[k][j] == 'T'):
                cT += 1
                if (cT > MaxCharVal[j]):
                    MaxCharVal[j] = cT
                    MaxChar[j] = 'T'
            elif (DNACut[k][j] == 'G'):
                cG += 1
                if (cG > MaxCharVal[j]):
                    MaxCharVal[j] = cG
                    MaxChar[j] = 'G'
            else:
                cC += 1
                if (cC > MaxCharVal[j]):
                    MaxCharVal[j] = cC
                    MaxChar[j] = 'C'
    ResultScore = sum(MaxCharVal)
    return ResultScore,MaxChar

def partialScore(s,i,DNA,l):
    iSeq=0
    DNACut=[]
    MaxChar=['A']*l
    MaxCharVal=[0]*l
    for iS in range(0,i):
        DNACut.append(list(DNA[iSeq][(s[iS]):((s[iS])+l)]))
        iSeq += 1
    #-- cal score
    for j in range(0,l):
        cA = 0
        cT = 0
        cG = 0
        cC = 0
        for k in range(0,len(DNACut)):
            #-- count char
            if (DNACut[k][j] == 'A'):
                cA += 1
                if (cA > MaxCharVal[j]):
                    MaxCharVal[j] = cA
                    MaxChar[j] = 'A'
            elif (DNACut[k][j] == 'T'):
                cT += 1
                if (cT > MaxCharVal[j]):
                    MaxCharVal[j] = cT
                    MaxChar[j] = 'T'
            elif (DNACut[k][j] == 'G'):
                cG += 1
                if (cG > MaxCharVal[j]):
                    MaxCharVal[j] = cG
                    MaxChar[j] = 'G'
            else:
                cC += 1
                if (cC > MaxCharVal[j]):
                    MaxCharVal[j] = cC
                    MaxChar[j] = 'C'
    ResultScore = sum(MaxCharVal)
    return ResultScore,MaxChar
    
def nextVertex(a,i,L,k):
    if i<L:
        a[i] = 0
        return (a,i+1)
    else:
        for j in range(L,0,-1):
            if a[j - 1] < k - 1:
                a[j - 1] = a[j - 1] + 1
                return (a,j)
    return (a,0)

def byPass(a,i,L,k):
    for j in range(i,0,-1):
        if a[j - 1] < k - 1:
            a[j - 1] = a[j - 1] + 1
            return (a,j)
    return (a,0)

def branchAndBoundMotifSearch(DNA,t,n,l):
    progress = "."
    countLoop = 0
    s = [0]*t
    scoreNow = 0
    BestScore = 0
    BestMotif = [0]*t
    i = 1
    while (i > 0):
        if (i < t):
            OptimisticScore = partialScore(s,i,DNA,l)[0]+(t-i)*l
            if (OptimisticScore < BestScore):
                s,i = byPass(s,i,t,(n - l + 1))
            else:
                s,i = nextVertex(s,i,t,(n - l + 1))
        else:
            scoreNow = score(s,DNA,l)[0]
            if (scoreNow > BestScore):
                BestScore = scoreNow
                BestMotif = s.copy()
            s,i = nextVertex(s,i,t,(n - l + 1))
        countLoop += 1
        #-- print progress
        if (countLoop%100000 == 0):
            os.system('cls')
            print("==================")
            print("Loading ",progress)
            print("==================")
            if (len(progress) == 10):
                progress = "."
            else:
                progress += "."
                
    Consensus = score(BestMotif,DNA,l)[1]
    ResultBestMotif = [x+1 for x in BestMotif]
    return countLoop,ResultBestMotif,BestScore,Consensus

def greedyMotifSearch(DNA,t,n,l):
    countLoop = 0
    BestMotif = [0]*t
    s = [0]*t
    for s[0] in range(0,(n-l+1)):
        for s[1] in range(0,(n-l+1)):
            if (partialScore(s,2,DNA,l)[0] > partialScore(BestMotif,2,DNA,l)[0]):
                BestMotif[0] = s[0]
                BestMotif[1] = s[1]
            countLoop += 1
    s[0] = BestMotif[0]
    s[1] = BestMotif[1]
    for i in range(2,t):
        for s[i] in range(0,(n-l+1)):
            if (partialScore(s,i+1,DNA,l)[0] > partialScore(BestMotif,i+1,DNA,l)[0]):
                BestMotif[i] = s[i]
            countLoop += 1
        s[i] = BestMotif[i]
    #print(countLoop)
    BestScore = score(BestMotif,DNA,l)[0]
    Consensus = score(BestMotif,DNA,l)[1]
    ResultBestMotif = [x+1 for x in BestMotif]   
    
    return countLoop,ResultBestMotif,BestScore,Consensus

#============================= 
    
def main(argv):
    if (len(sys.argv) == 4):
        FileName = sys.argv[1]
        if (os.path.exists('./' + FileName)):
            fo = open(str(FileName))
            DNA=[]
            for row in fo:
                if (row[0] != '>'):
                    DNA.append(row.replace('\n',''))
            fo.close()
            TypeMotif = sys.argv[2]
            l = int(str(sys.argv[3]))
            n = len(DNA[0])
            t = len(DNA)
            if (TypeMotif.upper() == "B"):
                countLoop,ResultBestMotif,BestScore,Consensus = branchAndBoundMotifSearch(DNA,t,n,l)
            elif (TypeMotif.upper() == "G"):
                countLoop,ResultBestMotif,BestScore,Consensus = greedyMotifSearch(DNA,t,n,l)
            else:
                print("error: Motif finding type must be B or G only.\n")
                exit()
            os.system('cls')
            print("Loop :",countLoop)
            print("BestMotif :",ResultBestMotif)
            print("BestScore :",BestScore)
            print("Consensus",Consensus)    
        else:
            print("error: file",FileName,"not found!\n")
            exit()
    else:
        print("usage: python a1-motif-600632014.py [fasta inputfile] [type of motif finding] [length of sequence].\nPlease, Try again.\n")

if __name__ == "__main__":
	main(sys.argv)

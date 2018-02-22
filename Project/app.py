
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

def nextLeaf(a,L,k):
    a=[0]+a
    for i in range(L,0,-1):
        if a[i]<k :
            a[i]=a[i]+1
            a.pop(0)
            return a
        a[i]=1
    a.pop(0)
    return a
    
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
        #if (countLoop%10000 == 0):
            #print(countLoop+1,"score :",scoreNow,"best score :",BestScore,s,"best :",BestMotif)
    Consensus = score(BestMotif,DNA,l)[1]
    ResultBestMotif = [x+1 for x in BestMotif]
    #print("=== run finish ===")
    return countLoop,ResultBestMotif,BestScore,Consensus

#============================= 
    
n = 60
l = 10
t = 5
fo = open('test2.fasta')
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()

countLoop,ResultBestMotif,BestScore,Consensus = branchAndBoundMotifSearch(DNA,t,n,l)

print("Loop :",countLoop)
print("BestMotif :",ResultBestMotif)
print("BestScore :",BestScore)
print("Consensus",Consensus)

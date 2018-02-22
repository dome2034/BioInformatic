
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
    return ResultScore

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
    return ResultScore

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
    BestScore = 0
    i = 1
    while (i > 0):
        if (i < t):
            OptimisticScore = partialScore(s,i,DNA,l)+(t-i)*l
            if (OptimisticScore < BestScore):
                s,i = byPass(s,i,t,(n - l + 1))
                print(countLoop+1,OptimisticScore,BestScore,(s,i),"by")
            else:
                s,i = nextVertex(s,i,t,(n - l + 1))
                print(countLoop+1,OptimisticScore,BestScore,(s,i),"next1")
        else:
            if (score(s,DNA,l) > BestScore):
                BestScore = score(s,DNA,l)
                BestMotif = s
            s,i = nextVertex(s,i,t,(n - l + 1))
            print(countLoop+1,OptimisticScore,BestScore,(s,i),"next2")
        countLoop += 1
    print(BestScore)
    return BestMotif

#============================= 
    
#s0 = [1,1,11,11]
#n = 28
#l = 8
#t = 4
n = 60
l = 10
t = 5
fo = open('test2.fasta')
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()

#print("nextLeaf: ",nextLeaf([1,1,1,2],4,2))
#print("nextVertex: ",nextVertex([1,1,1,1,1],1,5,51))
#print("byPass: ",byPass([1,2,2,2],3,4,2))
#print("Full Score : ",score(s0,DNA,l))
#print("Optimistic Score : ",partialScore(s0,1,DNA,l,t))

print(branchAndBoundMotifSearch(DNA,t,n,l))

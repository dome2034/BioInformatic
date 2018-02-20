
# Function definition is here
def score(s,DNA,l):
    iDNA=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    for row in range(0,len(s)):
        DNACut.append(DNA[iDNA][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[iDNA][(s[row]-1):((s[row]-1)+l)])
        iDNA+=1
        j=0
        for DNAChar in DNACutCal:            
            if (DNAChar == 'A'):
                A[j]+=1
            elif (DNAChar == 'T'):
                T[j]+=1
            elif (DNAChar == 'G'):
                G[j]+=1
            else:
                C[j]+=1
            j+=1
            
    ConsensusVal=[0]*l
    for k in range(l):
        Max = 0
        if(A[k] > Max):
            Max = A[k]
        if(T[k] > Max):
            Max = T[k]
        if(G[k] > Max):
            Max = G[k]
        if(C[k] > Max):
            Max = C[k]
        ConsensusVal[k] = Max
    ResultScore = sum(ConsensusVal)
    return ResultScore

def partialScore(s,i,DNA,l,t):
    iDNA=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    for row in range(0,i):
        DNACut.append(DNA[iDNA][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[iDNA][(s[row]-1):((s[row]-1)+l)])
        iDNA+=1
        j=0
        for DNAChar in DNACutCal:            
            if (DNAChar == 'A'):
                A[j]+=1
            elif (DNAChar == 'T'):
                T[j]+=1
            elif (DNAChar == 'G'):
                G[j]+=1
            else:
                C[j]+=1
            j+=1
            
    ConsensusVal=[0]*l
    for k in range(l):
        Max = 0
        if(A[k] > Max):
            Max = A[k]
        if(T[k] > Max):
            Max = T[k]
        if(G[k] > Max):
            Max = G[k]
        if(C[k] > Max):
            Max = C[k]
        ConsensusVal[k] = Max
    ResultScore = sum(ConsensusVal)+(t-i)*l
    print("Partial Score : ",sum(ConsensusVal))
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
    a=[0]+a
    if i<L:
        a[i]+1
        return (a,i+1)
    else:
        for j in range(L,0,-1):
            if a[j] < k:
                a[j]=a[j]+1
                a.pop(0)
                return (a,j)
    a.pop(0)
    return (a,0)

def byPass(a,i,L,k):
    a=[0]+a
    for j in range(i,0,-1):
        if a[j] < k:
            a[j] = a[j] +1
            a.pop(0)
            return (a,j)
    a.pop(0)
    return (a,0)

def branchAndBoundMotifSearch(DNA,t,n,l):
    s = [1,1,1,1]
    BestScore = 0
    i = 1
    while (i > 0):
        if (i < t):
            OptimisticScore = partialScore(s,i,DNA,l,t)
            if (OptimisticScore < BestScore):
                (s,i) = byPass(s,i,t,(n - l + 1)))
            else:
                (s,i) = nextVertex(s,i,t,(n - l + 1)))
        else:
            if (score(s,DNA,l) > BestScore):
                BestScore = score(s,DNA,l)
                BestMotif = s
            (s,i) = nextVertex(s,i,t,(n - l + 1)))
    return BestMotif
#============================= 
    
s0 = [1,1,11,11]
s1 = [1]
l = 8
t = 4
fo = open('test.fasta')
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()

#print("nextLeaf: ",nextLeaf([1,1,1,2],4,2))
#print("nextVertex: ",nextVertex([1,1,1,2],4,4,2))
#print("byPass: ",byPass([1,2,2,2],3,4,2))
print("Full Score : ",score(s0,DNA,l))
print("Optimistic Score : ",partialScore(s0,1,DNA,l,t))


# Function definition is here
def score(s,l,DNA):
    i=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    for row in range(0,len(s)):
        DNACut.append(DNA[i][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[i][(s[row]-1):((s[row]-1)+l)])
        i+=1
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
    for i in range(l):
        Max = 0
        if(A[i] > Max):
            Max = A[i]
        if(T[i] > Max):
            Max = T[i]
        if(G[i] > Max):
            Max = G[i]
        if(C[i] > Max):
            Max = C[i]
        ConsensusVal[i] = Max
    ResultScore = sum(ConsensusVal)
    return ResultScore

def partialScore(s,l,t,DNA):
    i=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    for row in range(0,len(s)):
        DNACut.append(DNA[i][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[i][(s[row]-1):((s[row]-1)+l)])
        i+=1
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
    
    for i in range(l):
        Max = 0
        if(A[i] > Max):
            Max = A[i]
        if(T[i] > Max):
            Max = T[i]
        if(G[i] > Max):
            Max = G[i]
        if(C[i] > Max):
            Max = C[i]
        ConsensusVal[i] = Max
    ResultScore = sum(ConsensusVal)+(t-len(s))*l
    print("Partial Score : ",sum(ConsensusVal))
    return ResultScore
#============================= 
    
s0=[1,1,11,11]
s1=[1]
l=8
t = 4
fo = open('test.fasta')
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()

print("Full Score : ",score(s0,l,DNA))
print("Optimistic Score : ",partialScore(s1,l,t,DNA))

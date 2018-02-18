
# Function definition is here
def score(s,l,DNA):
    i=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    print(len(DNA))
    for row in range(0,len(DNA)):
        DNACut.append(DNA[i][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[i][(s[row]-1):((s[row]-1)+l)])
        i+=1
        j=0
        print(DNACutCal)
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
            
    Consensus=['A']*l
    ConsensusVal=[0]*l
    for i in range(l):
        Max = 0
        if(A[i] > Max):
            Max = A[i]
            Consensus[i]='A'
        if(T[i] > Max):
            Max = T[i]
            Consensus[i]='T'
        if(G[i] > Max):
            Max = G[i]
            Consensus[i]='G'
        if(C[i] > Max):
            Max = C[i]
            Consensus[i]='C'
        ConsensusVal[i] = Max
    ResultScore = sum(ConsensusVal)
    print("A : ",A)
    print("T : ",T)
    print("G : ",G)
    print("C : ",C)
    print("Consensus : ",Consensus)
    print("ConsensusVal : ",ConsensusVal)
    return ResultScore

def partialScore(s,l,t,DNA):
    i=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    print(l)
    for row in range(0,len(s)):
        DNACut.append(DNA[i][(s[row]-1):((s[row]-1)+l)])
        DNACutCal=(DNA[i][(s[row]-1):((s[row]-1)+l)])
        i+=1
        j=0
        print(DNACutCal)     
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
        
    Consensus=['A']*l
    ConsensusVal=[0]*l
    
    for i in range(l):
        Max = 0
        if(A[i] > Max):
            Max = A[i]
            Consensus[i]='A'
        if(T[i] > Max):
            Max = T[i]
            Consensus[i]='T'
        if(G[i] > Max):
            Max = G[i]
            Consensus[i]='G'
        if(C[i] > Max):
            Max = C[i]
            Consensus[i]='C'
        ConsensusVal[i] = Max
    ResultScore = sum(ConsensusVal)
    OptScore = (t-len(s))*l
    print("A : ",A)
    print("T : ",T)
    print("G : ",G)
    print("C : ",C)
    print("Consensus : ",Consensus)
    print("ConsensusVal : ",ConsensusVal)
    print("Consensus Score : ",ResultScore)
    fullScore = ResultScore+OptScore
    return fullScore

#============================= 
s0=[9,13,2,15]
s1=[9,13]
l=6
t = 4
fo = open('test.fasta')
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()

print("Consensus Score : ",score(s0,l,DNA))
print("Optimistic Score : ",partialScore(s1,l,t,DNA))

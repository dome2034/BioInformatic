
# Function definition is here
def score(s,DNA):
    l=8
    i=0
    DNACut=[]
    A=[0]*l
    T=[0]*l
    G=[0]*l
    C=[0]*l
    for row in s:
        DNACut.append(DNA[i][(row-1):((row-1)+l)])
        DNACutCal=(DNA[i][(row-1):((row-1)+l)])
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
    Consensus=['A']*8
    ConsensusVal=[0]*8
    for i in range(8):
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
    print("A : ",A)
    print("T : ",T)
    print("G : ",G)
    print("C : ",C)
    print("Consensus : ",Consensus)
    print("ConsensusVal : ",ConsensusVal)
    print("Consensus Score : ",sum(ConsensusVal))
    return DNACut,A,T,G,C
#=============================

s=[1,1,1]
fo = open('brca1-human.fasta')
fo.readline()
DNA=[]
for row in fo:
    DNA.append(row.replace('\n',''))
fo.close()


score(s,DNA)
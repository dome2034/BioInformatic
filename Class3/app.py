

# Function definition is here
def nextLeaf(a,L,k):
    for i in range(L,0,-1):
        if a[i]<k :
            a[i]=a[i]+1
            return a
        a[i]=1
    return a
    
def nextVertex(a,i,L,k):
    if i<L:
        a[i]+1
        return (a,i+1)
    else:
        for j in range(L,0,-1):
            if a[j] < k:
                a[j]=a[j]+1
                return (a,j)
    return (a,0)

def byPass(a,i,L,k):
    for j in range(i,0,-1):
        if a[j] < k:
            a[j] = a[j] +1
            return (a,j)
    return (a,0)
    
#print(nextLeaf([0,1,1,1,2],4,2))
#print(nextVertex([0,1,1,1,2],4,4,2))
print(byPass([0,1,2,2,2],3,4,2))
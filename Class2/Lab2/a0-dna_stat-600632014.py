import sys

# Function definition is here
def percentText(SourceDNA,Text): 
    SourceDNA.count(Text)*100/len(SourceDNA)
    return SourceDNA.count(Text)*100/len(SourceDNA)

fo = open(str(sys.argv[1]))
fo.readline()
DNA = ''
for row in fo:
    DNA = DNA + row
fo.close()

DNA = DNA.replace('\n','')

print("A = ", percentText(DNA,'A'))
print("C = ", percentText(DNA,'C'))
print("G = ", percentText(DNA,'G'))
print("T = ", percentText(DNA,'T'))

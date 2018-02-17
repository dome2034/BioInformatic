import random

DNARange = int(input("input number of DNA: "))
DNA = ''
for DNARange in range(DNARange):
    DNA = DNA + random.choice('ATGC')

print("DNA =",DNA)
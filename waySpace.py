import sys

from datetime import datetime
startTime = datetime.now()

# Arrays to contain the resulting friend network
tier1 = []
tier2 = []
tier3 = []

#function that calculates the levenshtein distance
def levenshtein(a, b):
    # better to make these variables than repeatedly calling len
    magA = len(a)
    magB = len(b)
    D = [[0 for x in range(magB+1)]for x in range(2)]
    if (abs(magA-magB) > 1):
        D[0][len(line)] = 10
        return D
    for j in range(1, magB+1):
        D[0][j] = j
    for i in range(magA):
        D[1][0] = i+1
        for j in range(1, magB+1):
            m1 = D[0][j-1]
            if (a[i] != b[j-1]):
                m1 += 1
            m2 = D[0][j] + 1
            m3 = D[1][j-1] + 1
            D[1][j] = min(m1, m2, m3)
        D[0] = D[1]
        D[1] = [0 for x in range(magB+1)]
    return D

a = sys.argv[1]

with open('randomlist.txt', 'r') as f:
    for line in f:
        line = line.strip()
        lev = levenshtein(a, line)[0][len(line)]
        if lev < 2:
            tier1.append(line)
    for x in tier1:
        lev = levenshtein(a, x)[0][len(line)]
        if lev < 2:
            tier2. append(x)
    for x in tier2:
        lev = levenshtein(a, x)[0][len(line)]
        if lev < 2:
            tier3. append(x)

print datetime.now()-startTime
print tier1
print tier2
print tier3

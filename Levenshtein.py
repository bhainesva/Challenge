import sys

from datetime import datetime
startTime = datetime.now()

# Arrays to contain the resulting friend network
tier1 = []
tier2 = []
tier3 = []

a = sys.argv[1]

#function that calculates the levenshtein distance
def isClose(a, b, thresh):
    magA = len(a)
    magB = len(b)
    if (abs(magA-magB) > thresh):
        return False
    D = [[0 for x in range(magB+1)]for x in range(2)]
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
        if min(*D[1]) > thresh:
            return False
        D[0] = D[1]
        D[1] = [0 for x in range(magB+1)]
    return D[0][magB] <= thresh

cands = []
with open('randomlist.txt', 'r') as f:
    for word in f:
        word = word.strip()
        if isClose(a, word, 3):
            cands.append(word)
    
for word in cands:
    if isClose(a, word, 1):
        tier1.append(word)

for word in cands:
    if word not in tier1:
        for a in tier1:
            if isClose(a, word, 1):
                tier2.append(word)

for word in cands:
    if word not in tier2 and word not in tier1:
        for a in tier2:
            if isClose(a, word, 1):
                tier3.append(word)

print datetime.now() - startTime
print "TIER1: ", tier1
print "TIER2: ", tier2
print "TIER3: ", tier3

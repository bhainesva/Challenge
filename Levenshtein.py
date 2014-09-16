import sys

from datetime import datetime
startTime = datetime.now()

# Returns a boolean indicating whether the two strings
# a and b are within thresh steps of each other
def isClose(a, b, thresh):
    #Storing these values in variables to avoid repeated len() calls
    magA = len(a)
    magB = len(b)

    # There's no point computing the distance if we know it
    # has to be over the threshold
    if (abs(magA-magB) > thresh):
        return False

    # Initializes the two dimensional array where the work is done
    D = [[0 for x in range(magB+1)]for x in range(2)]

    # To turn an empty string into one of len(j) requires j edits
    for j in range(1, magB+1):
        D[0][j] = j

    for i in range(magA):
        D[1][0] = i+1
        for j in range(1, magB+1):

            # Substitution
            m1 = D[0][j-1]

            # If we're substituting 'x' for 'x' it doesn't count
            if (a[i] != b[j-1]):
                m1 += 1

            # Deletion
            m2 = D[0][j] + 1

            # Insertion
            m3 = D[1][j-1] + 1

            # Determines which path is the most efficient
            D[1][j] = min(m1, m2, m3)

        # If we've already taken more steps than the threshold
        # there's no point in continuing
        if min(*D[1]) > thresh:
            return False

        # Resets the working matrix
        D[0] = D[1]
        D[1] = [0 for x in range(magB+1)]

    return D[0][magB] <= thresh

# Arrays to contain the resulting friend network
tier1 = []
tier2 = []
tier3 = []

# User input word to create a network for
a = sys.argv[1]

# Array to hold candidates for being added to the network
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

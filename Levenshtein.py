import sys

from datetime import datetime

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

    # To turn an empty string into one of length j requires j edits
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


def extract(inList, exclude):
    out = []
    for word in inList:
        if word not in exclude:
            for a in exclude:
                if word not in out and isClose(a, word, 1):
                    out.append(word)
    return out

if __name__ == "__main__":
    startTime = datetime.now()
    # Array to contain the resulting friend network
    tiers = [[] for x in range(3)]

    # User input word to create a network for
    a = sys.argv[1]

    # Array to hold candidates for being added to the network
    cands = []

    # Reads in contents of wordlist and determines candidates
    with open('randomlist.txt', 'r') as f:
        for word in f:
            word = word.strip()
            if isClose(a, word, 3):
                cands.append(word)

    # Extracts the tiers from the possible candidates
    tiers[0] = extract(cands, [a])
    tiers[1] = extract(cands, tiers[0])
    tiers[2] = extract(cands, tiers[1])

    # Outputs running time
    print datetime.now() - startTime

    # Displays results
    print "INPUT: ", a
    print "TIER1: ", tiers[0]
    print "TIER2: ", tiers[1]
    print "TIER3: ", tiers[2]

import sys
import numpy as np

def main():
    gap = -1
    mismatch = -1
#    gap = -4
 #   mismatch = -5
    #ACACATGCATCATGACTATGCATGCATGACTGACTGCATGCATGCATCCATCATGCATGCATCGATGCATGCATGACCACCTGTGTGACACATGCATGCGTGTGACATGCGAGACTCACTAGCGATGCATGCATGCATGCATGCATGC
    #ATGATCATGCATGCATGCATCACACTGTGCATCAGAGAGAGCTCTCAGCAGACCACACACACGTGTGCAGAGAGCATGCATGCATGCATGCATGCATGGTAGCTGCATGCTATGAGCATGCAG
    args = sys.argv[1:]

    # Print the arguments
    print("Command-line arguments:")
    for arg in args:
        print(arg)

    # Initialize matrix
    x, y = args[0], args[1]
    lenx, leny = len(x), len(y)
    M = np.zeros((lenx + 1, leny + 1))
    M[:,0] = np.linspace(0, -lenx, lenx + 1)
    M[0,:] = np.linspace(0, -leny, leny + 1)
    print(M)

    # Compute values
    for j in range(0,leny):
        for i in range(0,lenx):
            if (x[i] == y[j]):
                match = 1
                #M[i+1,j+1] = best_previous + 1
            else:
                match = mismatch
                #M[i+1,j+1] = best_previous - 1
            best_previous = np.max(np.array((M[i,j] + match, M[i+1,j] + gap, M[i,j+1] + gap)))
            M[i+1,j+1] = best_previous
    print(M)
    print("score:", M[lenx,leny])
    
    # Find sequence alignment
    align1, align2 = "", ""
    i, j = lenx, leny

    while i > 0 or j > 0:
        current_score = M[i][j]
        if i > 0 and j > 0 and current_score == M[i-1][j-1] + (1 if x[i-1] == y[j-1] else -1):
            align1 += x[i-1]
            align2 += y[j-1]
            i -= 1
            j -= 1
        elif i > 0 and current_score == M[i-1][j] - 1:
            align1 += x[i-1]
            align2 += "-"
            i -= 1
        else:
            align1 += "-"
            align2 += y[j-1]
            j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    print(align1)
    print(align2)
if __name__ == "__main__":
    main()


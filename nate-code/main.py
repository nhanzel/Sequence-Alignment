def sequence_alignment_score(X, Y, gap_cost, mismatch_cost): # Needleman-Wunsch algorithm
    m, n = len(X), len(Y)
    
    # Initialize the matrix
    a = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill in first row and first column
    for i in range(1, m + 1):
        a[i][0] = i * gap_cost
    for j in range(1, n + 1):
        a[0][j] = j * gap_cost
    
    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                match_cost = 0 # match
            else:
                match_cost = -mismatch_cost
            
            a[i][j] = min(a[i - 1][j - 1] + match_cost,   # match/mismatch
                           a[i - 1][j] + gap_cost,        # gap in Y
                           a[i][j - 1] + gap_cost)        # gap in X
            
    # Traceback to find the optimal alignment
    aligned_X = []
    aligned_Y = []
    i, j = m, n
    
    while i > 0 and j > 0:
        # Checking if moving diagonally back is our best option
        if X[i - 1] == Y[j - 1] or a[i][j] == a[i - 1][j - 1] + (0 if X[i - 1] == Y[j - 1] else mismatch_cost):
            aligned_X.append(X[i - 1])
            aligned_Y.append(Y[j - 1])
            i -= 1
            j -= 1
        elif a[i][j] == a[i - 1][j] + gap_cost:
            aligned_X.append(X[i - 1])
            aligned_Y.append('_')
            i -= 1
        else:
            aligned_X.append('_')
            aligned_Y.append(Y[j - 1])
            j -= 1
    
    # Pad either sequence if there is a size mismatch
    while i > 0:
        aligned_X.append(X[i - 1])
        aligned_Y.append('_')
        i -= 1
    while j > 0:
        aligned_X.append('_')
        aligned_Y.append(Y[j - 1])
        j -= 1
    aligned_X.reverse()
    aligned_Y.reverse()
    
    print("Aligned X: ", ''.join(aligned_X))
    print("Aligned Y: ", ''.join(aligned_Y))
    
    return a[m][n] # score

# Read input data
with open('data.txt') as f:
    f.readline() # we don't need the lengths
    gap_cost, mismatch_cost = map(int, f.readline().split())
    X = f.readline().strip()
    Y = f.readline().strip()
    alignment_score = sequence_alignment_score(X, Y, gap_cost, mismatch_cost)
    print("\n")
    print(f"X: {X}")
    print(f"Y: {Y}")
    print(f"Gap Cost: {gap_cost}")
    print(f"Mismatch Cost: {mismatch_cost}")
    print(f"Alignment Score: {alignment_score}")

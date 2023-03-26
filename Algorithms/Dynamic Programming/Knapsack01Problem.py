#0-1 Knapsack problem - Pseudo Polynomial Time
def knapsack_prob(val,wt,w):
    n = len(wt)
    mem = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] > j: mem[i][j] = mem[i-1][j]
            else:
                mem[i][j] = max(val[i-1] + mem[i-1][j-wt[i-1]], mem[i-1][j])
    return mem[n][w]

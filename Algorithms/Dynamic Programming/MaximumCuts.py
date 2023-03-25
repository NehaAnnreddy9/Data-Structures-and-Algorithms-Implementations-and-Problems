#Maximum Cuts of a rod(DP Tabulation)-
def max_cut(a,b,c,n):
    mem = [-1 for i in range(n+1)]
    mem[0] = 0
    for i in range(1,n+1):
        if (i-a >= 0): mem[i] = max(mem[i],mem[i-a])
        if (i-b >= 0): mem[i] = max(mem[i],mem[i-b])
        if (i-c >= 0): mem[i] = max(mem[i],mem[i-c])
        if mem[i] != -1: mem[i]+=1   
    return mem[n]

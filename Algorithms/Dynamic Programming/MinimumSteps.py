#Minimum steps to reach end-
def min_steps(arr):
    n = len(arr)
    minm = [math.inf for i in range(n)]
    minm[0] = 0
    if n > 1: minm[1] = 1
    for i in range(2,n):
        sml = math.inf
        for j in range(i):
            if i - j <= arr[j]:
                minc = minm[j] + 1
                sml = min(sml,minc)
        minm[i] = sml
    return minm[n-1]            

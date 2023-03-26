#Minimum coins to reach value-Naive Solution-
import math
def min_coins(arr,t):
    if t == 0: return 0
    sml = math.inf
    for i in range(len(arr)):
        if arr[i] <= t:
            minc = min_coins(arr,t-arr[i])
            if minc != math.inf: sml = min(sml,minc+1)
    return sml
  
#Minimum coins to reach value-DP Memoized Solution-
import math
def w_min_coins(arr,t):
    mem = [-1 for i in range(t+1)]
    return dp_min_coins(arr,t,mem)

def dp_min_coins(arr,t,mem):
    if mem[t] != -1: return mem[t]
    if t == 0: return 0
    sml = math.inf
    for i in range(len(arr)):
        if arr[i] <= t:
            minc = dp_min_coins(arr,t-arr[i],mem)
            if minc!= math.inf: sml = min(sml,minc+1)
    mem[t] = sml
    return mem[t]
  
#Minimum coins to reach value-DP Tabulation Solution-
import math
def t_min_coins(arr,t):
    mem = [math.inf for i in range(t+1)]
    mem[0] = 0
    for i in range(1,t+1):
        sml = math.inf
        for j in range(len(arr)):
            if arr[j] <= i:
                minc = 1 + mem[i - arr[j]]
                sml = min(sml,minc)
        mem[i] = sml
    return mem[t]

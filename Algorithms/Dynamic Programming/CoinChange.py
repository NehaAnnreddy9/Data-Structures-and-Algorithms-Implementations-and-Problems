#Naive Solution-
def W_coin_change(arr,target):
    arr.sort()
    return coin_change(arr,target,0,0)

def coin_change(arr,target,sum,res):
    if sum == target: 
        return res + 1
    elif sum > target: return res
    for i in range(len(arr)):
        sum = sum + arr[i]
        res = coin_change(arr[i:],target,sum,res)
        sum = sum - arr[i]  
    return res
  
 #DP Tabulation-
def dp_coin_change(arr,n):
    mem = [[0 for j in range(len(arr)+1)] for i in range(n+1)]
    for j in range(len(arr)+1): mem[0][j] = 1
    for i in range(1,n+1):   
        for j in range(1,len(arr)+1):
            mem[i][j] = mem[i][j-1]
            if arr[j-1] <= i:
                mem[i][j] = mem[i][j] + mem[i - arr[j-1]][j]  
    return mem[n][len(arr)]

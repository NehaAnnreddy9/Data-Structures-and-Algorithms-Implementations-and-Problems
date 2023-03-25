#Longest Increasing Subsequence-
def liss(arr):
    n = len(arr)
    st = [0 for i in range(n)]
    for i in range(n):
        largest = 0
        for j in range(i): 
            if arr[j] < arr[i]:
                if st[j]+1 > largest: largest = st[j] + 1
        if largest == 0: st[i] = 1
        else: st[i] = largest
    print(st)
    return max(st)             

#Longest common subseq O(n) solution-
def w_lcs(s1,s2):
    if len(s1) >= len(s2):
        lcss = lcs(s1,s2,len(s1) - 1,len(s2) - 1)
    else:
        lcss = lcs(s2,s1,len(s2) - 1,len(s1) - 1)
    print(lcss)
    res = max(lcss, key = len)
    return res
    
def lcs(s1,s2,m,n):
    if m == 0:
        arr = []
        for i in range(n+1):
            if s1[0] == s2[i]: arr.append(s1[0])
        return arr
    else:
        arr = lcs(s1,s2,m-1,n)
        ind = -1
        for i in range(n+1):
            if s1[m] == s2[i]: ind = i
        if ind == -1:
            return arr
        else:
            flg = 0
            la = len(arr)
            for j in range(la):
                l = len(arr[j]) - 1
                for k in range(l,-1,-1):
                    if s2.find(arr[j][k]) < ind:
                        if k == l:
                            arr[j] = arr[j] + s1[m]
                        else:
                            arr.append(arr[j][0:k+1] + s1[m])
                        flg = 1
                        break
            if flg == 0: arr.append(s1[m])
            return arr

#Dynamic Programming O(m*n) Soln-
def w_lcs(s1,s2):
    arr = [[-1 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    lcss = lcs(s1,s2,len(s1),len(s2),arr)
    print(arr)
    return lcss
    
def lcs(s1,s2,m,n,arr):
    if arr[m][n] != -1: return arr[m][n]
    if m == 0 or n == 0: return 0
    else:
        if s1[m-1] == s2[n-1]:
            arr[m][n] =  1 + lcs(s1,s2,m-1,n-1,arr)
        else:
           arr[m][n] = max(lcs(s1,s2,m-1,n,arr),lcs(s1,s2,m,n-1,arr))
    return arr[m][n]

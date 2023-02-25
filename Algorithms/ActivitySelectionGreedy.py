def Activity_Selection_Greedy(arr):
    arr.sort(key=lambda x: x[1])
    sol = [arr[0]]
    res = 1
    e = arr[0][1]
    for i in range(1,len(arr)):
        if (arr[i][0]>= e): #Not overlapping
            res = res + 1
            sol.append(arr[i])
            e = arr[i][1]
    return res,sol
def Selection_sort(arr):
    size = len(arr)
    if  size == 1: return arr
    for i in range(size-1):
        least = i
        for j in range(i+1,size):
            if arr[j] < arr[least]: 
                least = j
        if i!=least: arr[i],arr[least] = arr[least],arr[i]
    return arr
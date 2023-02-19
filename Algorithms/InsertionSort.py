def Insertion_sort(arr):
    size = len(arr)
    if  size == 1: return arr
    for i in range(1,size):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
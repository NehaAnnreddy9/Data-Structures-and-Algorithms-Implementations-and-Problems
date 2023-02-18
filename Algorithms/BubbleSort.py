def swap(arr, j, k):
    temp = arr[j]
    arr[j] = arr[k]
    arr[k] = temp
    
def Bubble_sort(arr):
    size = len(arr)
    if  size == 1: return arr
    for i in range(size-1, 0, -1) :
        for j in range(i):
            if arr[j+1] < arr[j]:
                swap(arr, j, j+1)
    
    return arr

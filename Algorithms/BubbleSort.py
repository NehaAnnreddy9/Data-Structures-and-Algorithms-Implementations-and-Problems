def Bubble_sort(arr):
    size = len(arr)
    if  size == 1: return arr
    for i in range(size-1, 0, -1) :
        swapped = False
        for j in range(i):
            if arr[j+1] < arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

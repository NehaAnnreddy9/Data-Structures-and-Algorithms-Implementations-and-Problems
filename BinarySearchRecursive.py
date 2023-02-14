def BinarySearchRecur(arr,low,high,val):
    if len(arr) == 0: return -1
    if high < low: return -1
    mid = (low+high)//2
    if(arr[mid] == val): return mid
    elif(arr[mid] > val):
        return BinarySearchRecur(arr,low,mid-1,val)
    elif(arr[mid] < val):
        return BinarySearchRecur(arr,mid+1,high,val)

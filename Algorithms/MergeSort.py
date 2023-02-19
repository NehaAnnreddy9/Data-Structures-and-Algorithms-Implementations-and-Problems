def merge(arr,l,m,r):
    if l == m: arr1 = arr[l:l+1]
    else: arr1 = arr[l:m+1]
    if m+1 == r: arr2 = arr[m+1:m+2]
    else: arr2 = arr[m+1:r+1]
    i = j = 0
    k = l
    size1 = len(arr1)
    size2 = len(arr2)
    while i < size1 and j < size2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    if(i < size1):
        while(i < size1):
            arr[k] = arr1[i]
            i+=1
            k+=1
    elif(j < size2):
        while(j <  size2):
            arr[k] = arr2[j]
            j+=1
            k+=1

def Merge_sort(arr,l,r):
    if r>l:
        m = l + ((r-l)//2)
        Merge_sort(arr,l,m)
        Merge_sort(arr,m+1,r)
        merge(arr,l,m,r)
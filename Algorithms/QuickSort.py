#Lomuto Partition -
import random

def l_partition(arr,l,h):
    pivot_index = random.randint(l, h)
    arr[pivot_index], arr[h] = arr[h], arr[pivot_index]
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] < pivot:
            i+= 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1
    
def Quick_sort_lp(arr,l,h):
    if h > l:
        p = l_partition(arr,l,h)
        Quick_sort_lp(arr,l,p-1)
        Quick_sort_lp(arr,p+1,h)


#Hoare's Partition -
def h_partition(arr,l,h):
    pivot_index = random.randint(l, h)
    arr[pivot_index], arr[l] = arr[l], arr[pivot_index]
    pivot = arr[l]
    i = l-1
    j = h+1
    while(True):
        while(True):
            i+=1
            if arr[i] >= pivot: break
        while(True):
            j-=1
            if arr[j] <= pivot: break   
        if i >= j: return j
        arr[i], arr[j] = arr[j], arr[i]
    
def Quick_sort_hp(arr,l,h):
    if h > l:
        p = h_partition(arr,l,h)
        Quick_sort_hp(arr,l,p)
        Quick_sort_hp(arr,p+1,h)
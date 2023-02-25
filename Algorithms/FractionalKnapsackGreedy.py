def max_unit(a):
    return a[1]//a[0]
    
def fractional_knapsack_greedy(arr,capacity):
    arr = sorted(arr,key=max_unit,reverse=True)
    max_val = 0
    
    for i in range(len(arr)):
        item_w = arr[i][0]
        item_v = arr[i][1]
        if capacity == 0:
            break
        elif item_w <= capacity:
            capacity = capacity - item_w
            max_val+= item_v
        elif item_w > capacity:
            max_val+= ((capacity/item_w) * item_v)
            break
        
    return max_val
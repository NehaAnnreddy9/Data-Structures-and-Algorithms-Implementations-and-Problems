def Job_sequencing_greedy_1st(arr):
    arr = sorted(arr,key=lambda x: x[0])
    max_val = 0
    max_deadline = arr[-1][0] + 1
    for i in range(1,max_deadline):
        largest = 0
        index = -1
        for j in range(len(arr)):
            job_d = arr[j][0]
            job_p = arr[j][1]
            if job_d == i and job_p > largest:
                largest = job_p
                index = j
            elif job_d > i and largest == 0:
                largest = job_p
                index = j
        if index!=-1:
            max_val+= largest
            arr.pop(index)
                
    return max_val


def Job_sequencing_greedy_2nd(arr):
    max_d = 0
    for l in range(len(arr)):
        if max_d < arr[l][0]: max_d = arr[l][0]
    arr = sorted(arr,key=lambda x: x[1], reverse = True)
    max_val = 0
    slot_arr = [None] * max_d
    slot_arr[arr[0][0] - 1] = arr[0][1]
   
    for j in range(1,len(arr)):
        job_d = arr[j][0]
        job_p = arr[j][1]
        if slot_arr[job_d - 1] == None:
            slot_arr[job_d - 1] = job_p
        else:
            x = job_d - 2
            while x > -1:
                if slot_arr[x] == None:
                    slot_arr[x] = job_p
                    break
                else: x = x - 1
                
    for k in range(max_d):
        if slot_arr[k]!= None: max_val+=slot_arr[k]
                
    return max_val

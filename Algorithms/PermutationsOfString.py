#Naive Solution - 
def permute(str_final,l,r):
    if l==r:
        stn = ''.join(str_final)
        if stn.find("AB") == -1:
            print(stn)
    for i in range(l,r+1):
        str_final[i],str_final[l] = str_final[l],str_final[i]
        permute(str_final,l+1,r)
        str_final[i],str_final[l] = str_final[l],str_final[i]

#Solution with Backtracking -
def isSafe(arr,l,i,r):
    if l!=0 and arr[l-1] == "A" and arr[i] == "B":
        return False
    if l+1 == r and arr[i] == "A" and arr[l] == "B":
        return False
    return True
    
def permute(str_final,l,r):
    if l==r:
        stn = ''.join(str_final)
        print(stn)
    for i in range(l,r+1):
        if isSafe(str_final,l,i,r):
            str_final[i],str_final[l] = str_final[l],str_final[i]
            permute(str_final,l+1,r)
            str_final[i],str_final[l] = str_final[l],str_final[i]
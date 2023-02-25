#Function to return the largest possible number of n digits
#with sum equal to given sum.
class Solution:
    def largestNum(self,n,s):
        str_final = ''
        sum = s
        for i in range(n):
            if sum >= 9 and n > 1:
                sum = sum - 9
                str_final = str_final + "9"
            elif sum < 9 and sum > -1:
                str_final = str_final + str(sum)
                sum = 0
                
        if len(str_final) == 0 or sum!=0: return "-1"
        return str_final

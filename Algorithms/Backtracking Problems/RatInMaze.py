#Naive solution which prints the path backwards from destination to source and prints if there is path to destination or not -
def rat_in_maze(arr,i,j):
    if i > len(arr) - 1 or j > len(arr) - 1:
        return False
    if i == j and i == len(arr) - 1:
        print(i,j)
        return True
    if arr[i][j] == 0:
        return False
    x = rat_in_maze(arr,i+1,j) 
    y = rat_in_maze(arr,i,j+1) 
    if x == True or y == True: 
        print(i,j)
        return True
    else: return False
        
print(rat_in_maze([[1,0,0,0],[1,1,0,1],[1,0,0,0],[1,1,1,1]],0,0))
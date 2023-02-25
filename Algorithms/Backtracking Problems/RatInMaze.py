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
    
#Bactracking solution to print path from start to finish-        
def isSafe(arr,i,j):
    if i<len(arr) and j<len(arr) and arr[i][j] == 1:
        return True
        
def rat_in_maze(arr):
    n = len(arr)
    sol = [[0 for x in range(n)] for x in range(n)]
    if rat_in_maze_rec(arr,0,0,sol) == True:
        print(sol)
        return True
    else:
        return False
    
def rat_in_maze_rec(arr,i,j,sol):
    if i == j and i == len(arr) - 1:
        sol[i][j] = 1
        return True
    if isSafe(arr,i,j) == True:   
        sol[i][j] = 1
        if rat_in_maze_rec(arr,i+1,j,sol) == True: return True 
        elif rat_in_maze_rec(arr,i,j+1,sol) == True: return True
        sol[i][j] = 0
    return False

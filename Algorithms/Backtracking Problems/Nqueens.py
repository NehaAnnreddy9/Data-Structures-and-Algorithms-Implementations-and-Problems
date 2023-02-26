#N-queens naive solution-
def N_queens_rec(strn,n):
    if len(strn) == n:
        flg = 0
        for i in range(n-1):
            if strn[i] + 1 == strn[i+1] or strn[i] - 1 == strn[i+1]: #Need to consider more conditions - Incomplete solution
                flg = 1
                break
        if flg == 0: 
            print(strn)
            return True
    for j in range(n):
        if j not in strn:
            strn.append(j)
            if N_queens_rec(strn,n) == True: return True
            strn.pop()

#N-queens backtracking solution-
def isSafe(row,col,sol,n):
    for i in range(row):
        if sol[i][col] == "Q":
            return False
            
    j = col
    for i in range(row,-1,-1):
        if sol[i][j] == "Q":
            return False
        j-=1
        if j == -1: break
    i = row
    for j in range(col,n+1):
        if sol[i][j] == "Q":
            return False
        i-=1
        if i == -1: break
    return True
        
def N_queens(n):
    sol= [["." for x in range(n)] for x in range(n)]
    if N_queens_rec(0,sol,n-1) == True:
        print(sol)
        return True
    else: 
        return False

def N_queens_rec(row,sol,n):
    if row == n+1: return True
    for i in range(n+1):
        if isSafe(row,i,sol,n):
            sol[row][i] = "Q"
            if N_queens_rec(row+1,sol,n) == True: return True
            sol[row][i] = "."
    return False
 

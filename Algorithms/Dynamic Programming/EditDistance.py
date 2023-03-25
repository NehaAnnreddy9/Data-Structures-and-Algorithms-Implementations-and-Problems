def w_edit_dist(s1,s2):
    m = len(s1)
    n = len(s2)
    s1 = list(s1)
    s2 = list(s2)
    return edit_dist(s1,s2,m,n)

def edit_dist(s1,s2,m,n):
    if m == 0: return n
    elif n == 0: return m
    if s1[m-1] == s2[n-1]: return edit_dist(s1,s2,m-1,n-1)
    else:
        ins = edit_dist(s1,s2,m,n-1)
        dl = edit_dist(s1,s2,m-1,n)
        upd = edit_dist(s1,s2,m-1,n-1)
        return 1 + min(ins,dl,upd)

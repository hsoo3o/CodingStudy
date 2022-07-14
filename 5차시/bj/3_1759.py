import sys

def DFS(L,j):    
    if L == l:
        if any(str(code).find(i) != -1 for i in ['a','e','i','o','u']) and len(set(code)-set(['a','e','i','o','u'])) > 1:
            for i in code:
                print(i,end='')
            print()  
    else:
        for i in range(j,c):
            if ch[i] == 0:
                ch[i] = 1
                code[L] = string[i]
                DFS(L+1,i)
                ch[i] = 0


l,c = map(int,sys.stdin.readline().split())
string = list(sys.stdin.readline().split())
string.sort()
code = [0]*l

ch = [0] * c
DFS(0,0)
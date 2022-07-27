

def dfs(l,p):
    global cnt

    if l == n:
        cnt += 1
        for i in range(p):
            print(chr(int(num[i])+ord('A')-1),end='')
        print()
    else:
        for i in range(1,27):
            if code[l] == i:
                num[p] = i
                dfs(l+1,p+1)
            elif i >= 10 and code[l] == i// 10 and code[l+1]== i%10:
                num[p] = i
                dfs(l+2,p+1)
                


code = list(map(int,input()))
n = len(code)
code.insert(n,-1)
num = [0]*(n+3)
cnt = 0
dfs(0,0)
print(cnt)
# 재귀 함수 : stack 사용

def dfs(x):
    print(x)
    dfs(x-1)

if __name__=='__main__':
    n = int(input())
    dfs(n)
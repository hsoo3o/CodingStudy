def dfs(x):
    if x == 0:
        return # 함수에서 return 만 쓰면 함수를 종료시켜라 라는 의미도 있음
    else:
        dfs(x//2)
        print(x%2, end = " ")

if __name__=="__main__":
    n = int(input())
    dfs(n)
import sys
N = int(input())
numbers = sorted(list(map(int,input().split())))
# 전체 원소의 합 : total, sum : 내가 만든 부분 집합의 합
# 
M = len(numbers) // 2


def dfs(L,sum): # L : index number, sum : 부분집합 누적
    if L == N:
        if sum==(total-sum):
            print("YES")
            sys.exit(0) # 프로그램 전체를 종료
    else:
        dfs(L+1,sum+numbers[L])
        dfs(L+1,sum)

total = sum(numbers)
dfs(0,0)
print("NO")
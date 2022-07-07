import sys

n,w,l = map(int,sys.stdin.readline().split())
t = list(map(int,sys.stdin.readline().split()))

ans = 1
bridge = []

cnt = 0
while t:
    if sum(bridge) + t[0] <= l:
        bridge.append(t.pop(0))
        cnt += 1
    else:
        bridge.pop(0)
        ans += cnt
        cnt = 1
    print(bridge)

    # cnt += 1
    
    print(ans)
    # print(bridge)
if len(bridge) <= w:
    ans += w
else:
    ans += 1
print(ans)
'''

9 5 5
2 2 2 2 1 1 1 1 1

4 2 10
7 4 5 6
'''

# # 정답 : 19

# 0 0 0 0 2
# 0 0 0 2 2
# 0 0 2 2 0
# 0 2 2 0 0
# 2 2 0 0 0
# 2 0 0 0 2
# 0 0 0 2 2

# 4 2 10
# 7 4 5 6

# 0 7 1
# 7 0 2
# 0 4 3
# 4 5 4 
# 5 0 5
# 0 6 6
# 6 0 7 
# 0 0 8



n,w,l = map(int,input().split())
t = list(map(int,input().split()))

ans = 1
bridge = []
cnt = 0
while t:
    ans += 1
    if bridge and t:
        if sum(bridge) + t[0] <= l:
            bridge.append(t.pop(0))    
        else:
            bridge.pop(0)
            if len(bridge) == 0:
                cnt += 1
    else:
        bridge.append(t.pop(0)) 
print(ans, cnt,bridge)
if bridge:
    ans += w

print(ans, cnt)
'''
9 5 5
2 2 2 2 1 1 1 1 1
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


n,w,l = map(int,input().split())
t = list(map(int,input().split()))

ans = 0
bridge = [0]*w
while bridge:
    ans += 1
    bridge.pop(0)
    if t:
        if sum(bridge) + t[0] <= l:
            bridge.append(t.pop(0))    
        else:
            bridge.append(0)
print(ans)

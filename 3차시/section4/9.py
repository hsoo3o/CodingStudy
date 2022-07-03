n = int(input())
num = list(map(int,input().split()))

ans = ''
res = 0
s = 0
e =n-1
if num[s] < num[e]:
        ans += 'L'
        res = num[0]
        s += 1
else:
    ans += 'R'
    res = num[-1]
    e -= 1


while s<=e:
    gl = num[s] - res
    gr = num[e] - res
    print(res+gl,res + gr)
    if res + gl == num[s]:
        ans += '1'
        res = num[s]
        s += 1
    elif res + gr == num[e]:
        ans += '2'
        res = num[e]
        e -= 1
    elif res + gr == num[s]:
        ans += '3'
        res = num[e]
        s += 1
    elif res + gl == num[e]:
        ans += '4'
        res = num[e]
        e -= 1
    else:
        s+=1
        e-=1
print(res)
print(ans)






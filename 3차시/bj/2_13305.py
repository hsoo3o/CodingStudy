n = int(input())
length  = list(map(int,input().split(' ')))
city = list(map(int,input().split(' ')))

ans = city[0]*length[0]
money = city[0]
for i in range(1,n-1):

    if city[i] < money:
        money = city[i]
    ans += (money*length[i]) 
print(ans)



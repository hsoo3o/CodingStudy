m = 3
n = "1 2 1 3 1 1 1 2"
n = n.replace(" ",'')
n = list(map(int,n))
num = 0
cnt = 0
for i in range(len(n)):
    for j in range(i,len(n)):
        num += n[j]
        print(n[j],num)
        if num == m:
            cnt += 1
            break
    num = 0
    
print(cnt)
from collections import Counter
w1 = Counter(input())
w2 = Counter(input())

str1 = dict()
str2 = dict()
for x in str1:
    str1[x] = str1.get(x,0) +1
for x in str2:
    str2[x] = str2.get(x,0) +1

for k,v in w1.items():
    try:
        if w2[k] != v:
            print("NO")
            break
        w2.pop(k)
    except:
        print("NO")
        break
else:
    if w2:
        print("NO")
    else:
        print("YES")



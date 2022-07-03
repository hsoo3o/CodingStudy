l = int(input())
box = list(map(int, input().split(' ')))
m = int(input())

box.sort()
s = 0
e = l-1
for _ in range(m):
    box[s] += 1
    box[e] -= 1
    box.sort()
    
print(box[-1]-box[0])
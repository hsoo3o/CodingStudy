k,w = map(int,input().split())
je = []

for _ in range(k):
    je.append(list(map(int,input().split())))

dy = [0] * (w+1)

for i in range(k):
    for j in range(je[i][0],w+1):
        if dy[j] < dy[j-je[i][0]] + je[i][1]:
            dy[j] = dy[j-je[i][0]] + je[i][1]

print(dy[-1])
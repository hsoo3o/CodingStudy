
def dfs(l):
    global min_,people
    if l == n:
        cha = max(people) - min(people)
        if cha <= min_:
            tmp = set()
            for x in people:
                tmp.add(x)
            if len(tmp) == 3:
                min_ = cha
    else:
        for p in range(3):
            people[p] += coin[l]
            dfs(l+1)
            people[p] -= coin[l]

n = int(input())
coin = []
for _ in range(n):
    coin.append(int(input()))

people = [0,0,0]
min_ = sum(coin)
dfs(0)
print(min_)
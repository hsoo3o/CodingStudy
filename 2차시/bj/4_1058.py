n = int(input())
people = []
mf = 0

ans = 0
for i in range(n):
    person = list(input())
    if person.count('Y') > mf:
        mf = person.count('Y')
    people.append(person)

if mf == n-1:
    print(n-1)
else:
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            elif people[i][j] == 'Y':
                cnt += 1
            elif people[i][j] == 'N':
                for k in range(n):
                    if people[j][k] == 'Y':
                        if people[k][i] == 'Y':
                            cnt += 1
                            break
        if cnt >= ans:
            ans = cnt
    print(ans)


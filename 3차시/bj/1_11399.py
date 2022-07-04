n = int(input())

people = list(map(int,input().split()))
people.sort()

time = 0
all_time = 0
for i in people:
    time += i
    all_time += time
print(all_time)

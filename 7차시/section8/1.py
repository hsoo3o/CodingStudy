N = int(input())

line = [0 for _ in range(N)] 

line[0] = 1
line[1] = 2

for i in range(2,N):
    line[i] = line[i-1] + line[i-2]

print(line[-1])
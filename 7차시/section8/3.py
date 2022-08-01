
n = int(input())

bridge = [0] * (n)

bridge[0] = 2
bridge[1] = 3

for i in range(2,n):
    bridge[i] = bridge[i-1] + bridge[i-2]

print(bridge[-1])
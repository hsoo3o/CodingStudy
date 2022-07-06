num,remove = input().split(' ')
num = list(map(int,num))
remove = int(remove)

stack = []

for i in num:
    while stack and remove > 0 and stack[-1] < i:
        stack.pop()
        remove -= 1
    stack.append()

if remove != 0:
    stack = stack[:-remove]

res = ''.join(map(str,stack))
print(res)

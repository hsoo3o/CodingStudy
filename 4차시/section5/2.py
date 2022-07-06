l = list(input())
stack = []
res = 0
for i in range(len(l)):
    if l[i] == '(':
        stack.append(i)
    else:
        if i == stack[-1] +1:
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
print(res)


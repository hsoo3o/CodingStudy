eq = list(input())
num = [str(i) for i in range(1,10)]
stack = []
for i in eq:
    if i in num:
        stack.append(i)
    elif i == '+':
        stack.append(int(stack.pop()) + int(stack.pop()))
    elif i == '-':
        stack.append(- int(stack.pop()) + int(stack.pop()))
    elif i == '*':
        stack.append(int(stack.pop()) * int(stack.pop()))
    elif i == '/':
        stack.append(1 / (int(stack.pop()) / int(stack.pop())))

print(stack[0])

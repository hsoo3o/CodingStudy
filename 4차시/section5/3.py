eq = list(input())
num = [str(i) for i in range(1,10)]

stack = []
res = ''
for i in eq:
    if i in num:
        res += i
    elif i == '(':
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            res += stack.pop()
        stack.pop()
    elif i in ['*','/']:
        while stack and stack[-1] in ['*','/']:
            res += stack.pop()
        stack.append(i)
    elif i in ['+','-']:
        while stack and stack[-1] in ['+','-','*','/'] :
            res += stack.pop()
        stack.append(i)

while stack:
    res += stack.pop()
print(res)

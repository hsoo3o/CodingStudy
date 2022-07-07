import sys
global s
def push(stack,x):
    global s
    stack.append(x)
    s += 1

def pop(stack):
    global s
    if stack:
        print(stack[-1])
        del stack[-1]
        s -= 1
    else:
        print(-1)

def size():
    global s
    print(s)

def empty(stack):
    if stack:
        print(0)
    else:
        print(1)

def top(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())
stack = []
s = 0
for _ in range(n):
    com = list(sys.stdin.readline().split())
    if com[0] == "push":
        push(stack, com[1])
    elif com[0] == "pop":
        pop(stack)
    elif com[0] == "size":
        size()
    elif com[0] == "empty":
        empty(stack)
    elif com[0] == "top":
        top(stack)
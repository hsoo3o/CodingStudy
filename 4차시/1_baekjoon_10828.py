# # Baekjoon 10828

# from sys import stdin
# N = int(stdin.readline())

# stack = []
# for i in range(N):
#     message = stdin.readline().split()
#     if message[0] == 'push':
#         stack.append(message[1])
#     elif message[0] == 'pop':
#         if len(stack) != 0:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif message[0] == 'size':
#         print(len(stack))
#     elif message[0] == 'empty':
#         print(1 if len(stack) == 0 else 0)
#     elif message[0] == 'top':
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
 
bridge = [0] * (w-1)
time = 1
bridge.append(trucks.pop(0))

 
while bridge:
    time += 1
    bridge.pop(0)

    if bridge and trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
    elif bridge and not trucks:
        pass

print(time)

# n, w, l = map(int, input().split())
# trucks = list(map(int, input().split()))
 
# bridge = [0] * w
# time = 0
 
# while bridge:
#     time += 1
#     bridge.pop(0)
#     if trucks:
#         if sum(bridge) + trucks[0] <= l:
#             bridge.append(trucks.pop(0))
#         else:
#             bridge.append(0)
# print(time)
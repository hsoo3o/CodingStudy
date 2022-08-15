import sys

def one(belt):
    for i in range(len(robot)):
        robot[i] += 1
    return  [belt[2*N-1]] + belt[0:2*N-1], [robot_place[N-1]] + robot_place[0:N-1]

def two():
    global ans
    for i in range(len(robot)):
        if robot[i] + 1 < N and conv[robot[i] +1] > 0 and robot_place[robot[i]+1] == 0:
            mov =  robot[i] + 1
            conv[mov] -= 1
            robot_place[mov] , robot_place[robot[i]] = 1,0
            robot[i] = robot[i] +1
            if conv[mov] == 0:
                ans += 1


def three():
    global ans
    if conv[0] > 0:
        robot_place[0] = 1
        robot.append(0)
        conv[0] -= 1
        if conv[0] == 0:
            ans += 1


N,K = map(int,sys.stdin.readline().split())
conv = list(map(int,sys.stdin.readline().split()))
robot_place = [0 for _ in range(N)]
robot = []

ans = 0
res = 0
while ans < K:
    res += 1
    conv,robot_place = one(conv)
    if robot_place[-1] == 1:
        robot_place[-1] = 0
        robot.pop(0)
    two()
    if robot_place[-1] == 1:
        robot_place[-1] = 0
        robot.pop(0)
    three()

print(res)
# Baekjoon 2841

from sys import stdin

N, M = list(map(int, stdin.readline().split()))

ans = 0
lines = [[] for _ in range(6)]

"""
    line 번째 줄에 가장 높은 fret이 input fret 보다 큰가?
        if 크면:
            input fret 보다 작거나 같을 때 까지 pop
        input fret == 가장 높은 fret: ans += 0
        input fret <  가장 높은 fret: ans += 1; input fret push into lines[line]
"""

for i in range(N):
    line, fret = list(map(int, stdin.readline().split()))
    line -= 1
    if len(lines[line]) > 0:
        if lines[line][-1] < fret:
            lines[line].append(fret)
            ans += 1
        else:
            while len(lines[line]) > 0:
                if lines[line][-1] <= fret:
                    break
                lines[line].pop()
                ans += 1
            if len(lines[line]) == 0:
                lines[line].append(fret) 
                ans += 1
            elif lines[line][-1] < fret:
                lines[line].append(fret) 
                ans += 1
    else:
        lines[line].append(fret) 
        ans += 1
print(ans)
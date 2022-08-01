# Baekjoon 1149

from sys import stdin

N = int(stdin.readline())

R = [0 for _ in range(N)]
G = [0 for _ in range(N)]
B = [0 for _ in range(N)]
RGB = []
for i in range(N):
    rgb = list(map(int, stdin.readline().split()))
    RGB.append(rgb)
    if i == 0:
        R[i] = rgb[0]
        G[i] = rgb[1]
        B[i] = rgb[2]
    elif i == 1:
        R[i] = min(G[i-1]+rgb[0], B[i-1]+rgb[0])
        G[i] = min(R[i-1]+rgb[1], B[i-1]+rgb[1])
        B[i] = min(G[i-1]+rgb[2], R[i-1]+rgb[2])
        pass
    else:
        R[i] = min(R[i-2]+RGB[i-1][1]+rgb[0], R[i-2]+RGB[i-1][2]+rgb[0], G[i-2]+RGB[i-1][2]+rgb[0], B[i-2]+RGB[i-1][1]+rgb[0])
        G[i] = min(G[i-2]+RGB[i-1][0]+rgb[1], G[i-2]+RGB[i-1][2]+rgb[1], R[i-2]+RGB[i-1][2]+rgb[1], B[i-2]+RGB[i-1][0]+rgb[1])
        B[i] = min(B[i-2]+RGB[i-1][1]+rgb[2], B[i-2]+RGB[i-1][0]+rgb[2], G[i-2]+RGB[i-1][0]+rgb[2], R[i-2]+RGB[i-1][1]+rgb[2])

print(min(R[-1], G[-1], B[-1]))
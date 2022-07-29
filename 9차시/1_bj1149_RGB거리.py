import sys
input = sys.stdin.readline
N = int(input())
RGB = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])

print(min(RGB[-1]))
# dp = [[] for _ in range(N)]
# ans = [0 for _ in range(N)]
# ans = 9999999999
# tmp = min(rgb[0])
# bidx = rgb[0].index(tmp)

# def dfs(rgb_,bidx,L,tmp):
#     global ans
#     if L == N:
#         if tmp < ans:
#             ans = tmp
#         return
#     rgb = rgb_[L]
#     now = min(rgb)
#     idx = rgb.index(now)
#     if idx != bidx:
#         tmp += now
#     else:
#         cnt = rgb.count(now)
#         while cnt > 1:
#             rgb[idx] = 1001
#             now = min(rgb)
#             idx = rgb.index(now)
#             if idx != bidx:
#                 tmp += now
#                 break
#             cnt = rgb.count(now)
#     L += 1
#     dfs(rgb_,idx,L,tmp)
# dfs(rgb,bidx,0,tmp)
# print(ans)


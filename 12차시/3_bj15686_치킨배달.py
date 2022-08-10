# 0 - 빈 칸, 1 - 집, 2 - 치킨집
# 치킨집 중 폐업 시키지 않을 치킨집을 최대 M개를 고르며, 도시의 치킨 거리를 가장 작게 하는 프로그램
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]

n_chicken = 0

# for _ in city:
#     n_chicken += _.count(2)
pos_chicken = []
pos_home = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            pos_chicken.append((r,c))
            n_chicken += 1
        elif city[r][c] == 1:
            pos_home.append((r,c))

dis = 0
cand = []
if n_chicken == M:
    for r_h,c_h in pos_home:
        dis_ch = 9999999
        for r_c,c_c in pos_chicken:
            tmp = abs(r_h-r_c) + abs(c_h-c_c)
            if tmp < dis_ch:
                dis_ch = tmp
        dis += dis_ch
else:
    for r_c,c_c in pos_chicken:
        rc_cand,cc_cand = 0,0
        dis = 0
        for r_h,c_h in pos_home:
            dis += abs(r_h-r_c) + abs(c_h-c_c)
            rc_cand,cc_cand = r_c,c_c
        cand.append([(rc_cand,cc_cand),dis])
    cand.sort(key=lambda x:x[-1])
    
    dis = 999999
    
    def chicken_distance(cand):
        d_chicken = 0
        for r_h,c_h in pos_home:
            dis = 99999
            for chicken in cand:
                r_c,c_c = chicken[0]
                tmp = abs(r_h-r_c) + abs(c_h-c_c)
                if tmp < dis:
                    dis = tmp
            d_chicken += dis
        return d_chicken
    candi = []
    visited = []
    def dfs(L):
        global dis,candi,visited
        print(candi)
        if len(candi) == M:
            if chicken_distance(candi) < dis:
                dis = chicken_distance(candi)
            return
        else:
            for i in range(len(cand)):
                if candi != []:
                    if cand[i] not in candi:
                        candi.append(cand[i])
                        dfs(L+1)
                        candi.pop()
                else:
                    candi.append(cand[i])
                    dfs(L+1)
                    candi.pop()
    dfs(0)

print(dis)
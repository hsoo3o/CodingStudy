# Baekjoon 21608

N = int(input())
pref = {}
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0
for i in range(N ** 2):
    line = list(map(int, input().rstrip().split(' ')))
    pref[line[0]] = line[1:]

classroom = [[0 for _ in range(N)] for _ in range(N)]

for student in pref:
    # 1
    place_score = [[0 for _ in range(N)] for _ in range(N)]
    max_candidates = []
    max_val = -1
    for i in range(N):
        for j in range(N):
            if classroom[i][j] in pref[student]:
                for k in range(4):
                    nr = i + dy[k]
                    nc = j + dx[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if classroom[nr][nc] == 0:
                            place_score[nr][nc] += 1
    for i in range(N):
        max_val_ = max(place_score[i])
        if max_val_ > max_val:
            max_candidates = []
            max_val = max_val_
            for j in range(N):
                if place_score[i][j] == max_val_ and classroom[i][j] == 0:
                    max_candidates.append([i,j])
        elif max_val_ == max_val:
            for j in range(N):
                if place_score[i][j] == max_val_ and classroom[i][j] == 0:
                    max_candidates.append([i,j])
    
    if len(max_candidates) > 1:
        # 2
        place_score = [0 for _ in range(len(max_candidates))]
        for i in range(len(max_candidates)):
            candidates = max_candidates[i]
            for k in range(4):
                nr = candidates[0] + dy[k]
                nc = candidates[1] + dx[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if classroom[nr][nc] == 0:
                        place_score[i] += 1
                        
        max_candidates_ = []
        max_val = max(place_score)
        for i in range(len(place_score)):
            if place_score[i] == max_val:
                max_candidates_.append(max_candidates[i])
                
        
        if len(max_candidates_) > 1:
            # 3
            max_candidates_.sort()
            classroom[max_candidates_[0][0]][max_candidates_[0][1]] = student
        else:
            classroom[max_candidates_[0][0]][max_candidates_[0][1]] = student
    else:
        classroom[max_candidates[0][0]][max_candidates[0][1]] = student

for i in range(N):
    for j in range(N):
        number_of_friends = 0
        for k in range(4):
            nr = i + dy[k]
            nc = j + dx[k]
            if 0 <= nr < N and 0 <= nc < N:
                if classroom[nr][nc] in pref[classroom[i][j]]:
                    number_of_friends += 1

        ans += int(pow(10, number_of_friends-1))
        
print(ans)
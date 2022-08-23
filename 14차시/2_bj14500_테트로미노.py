# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

# N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성

# 회전이나 대칭을 시켜도 된다.

# N,M = map(int,input().split())

# table = [list(map(int,input().split())) for _ in range(N)]

# t1 = [[0] * 4 for _ in range(4)]
# t1[0] = [1,1,1,1]

# t2 = [[1]*2 for _ in range(2)]

# t3 = [[0]*2 for _ in range(3)]
# t3[0] = [1,0]
# t3[1] = [1,0]
# t3[2] = [1,1]

# t4 = [[0]*3 for _ in range(2)]
# t4[0] = [1,1,1]
# t4[1] = [0,1,0]

# def rotate(m):
#     ret = list(zip(*m[::-1]))
#     return ret
 
# def transpose(m):
#     ret = list(zip(*m))
#     return ret

# # Utility Function
# def printMatrix(mat):
#     for row in mat:
#         print(row)

# printMatrix(t4)
# # Print modified matrix
# for i in range(4):
#     t4 = rotate(t4)
#     print("")
#     printMatrix(t4)

# t4 = transpose(t4)

# for i in range(4):
#     t4 = rotate(t4)
#     print("")
#     printMatrix(t4)

import sys
input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer
    # 종료조건1) 탐색을 계속 진행하여도 최댓값에 못 미치는 경우
    if total + max_val*(4-step) <= answer:
        return

    # 종료조건2) 블록 4개를 모두 활용한 경우
    if step == 4:
        answer = max(answer, total)
        return

    # 상하좌우 방향으로 블록 이어 붙여 나가기
    for dx, dy in d:
        nx = x + dx # 새로운 x 좌표
        ny = y + dy # 새로운 y 좌표
        # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 2번째 블록 연결 후 'ㅏ','ㅓ','ㅗ','ㅜ' 만들기
            if step == 2:
                visited[nx][ny] = True # 탐색기록
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False # 탐색기록 제거

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

N, M = map(int, input().split()) # 좌표의 행, 열 개수
board = [list(map(int, input().split())) for _ in range(N)] # 좌표별 값
max_val = max(map(max, board)) # 모든 좌표 중 최댓값
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌표 내 상하좌우
visited = [[False] * M for _ in range(N)] # 탐색여부 확인용
answer = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True # 탐색기록
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False # 탐색기록 제거
print(answer)
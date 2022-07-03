import sys

n,m = input().split(' ')
mat = [[0 for _ in range(10)] for _ in range(10)]
cnt = 1
for i in range(int(n)):
    x1,y1,x2,y2 = input().split(' ')
    
    mat[int(x1):int(x2)+1][int(y1):int(y2)+1] = [[cnt for _ in range(int(y2) - int(y1))] for _ in range(int(x2) - int(x1))]
    print([[cnt*(int(y2) - int(y1))]*(int(x1) - int(x2))])
    cnt += 1
    print(mat[int(x1):int(x2)+1][int(y1):int(y2)] )

import sys
from collections import Counter
sys.stdin.readline()
s = list(map(int,sys.stdin.readline().split()))
sys.stdin.readline()
c = list(map(int,sys.stdin.readline().split()))
cnt = Counter(s)
for i in c:
    if i in cnt:
        print(cnt[i],end=' ') 
    else:
        print(0,end=' ')   

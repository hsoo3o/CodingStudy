
def dfs(len_):
    if line[len_] > 0:
        return line[len_]
    if len_ == 1 or len_ == 2:
        return len_
    else:
        line[len_] = dfs(len_-1) + dfs(len_-2)
        return line[len_]

n = int(input())

line = [0] * (n+1)
print(dfs(n))
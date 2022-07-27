# 전위순회 : 부모 / 왼자식 / 오자식, 
# 중위순회 : 왼자식 / 부모 / 오자식, 쓰이는 적 별로 본 적 없음
# 후위순회 : 왼자식 / 오자식 / 부모, 병합 정렬에 사용

def dfs(v):
    if v > 7:
        return
    else:
        dfs(v*2)
        dfs(v*2+1)
        print(v,end=" ")

if __name__=="__main__":
    dfs(1)

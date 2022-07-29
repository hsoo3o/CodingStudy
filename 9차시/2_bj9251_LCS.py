first = input()
second = input()

l1 = len(first)
l2 = len(second)
LCS = []

ans = 999999

def dfs1(word1, word2, L,LCS):
    global ans
    if L == l1:
        tmp = "".join(LCS)
        print(LCS)
        if len(LCS) < int(ans):
            ans = tmp
        return
    else:
        # print(list(word1)[L])
        # print("LCS:",LCS)
        LCS1 = LCS.copy()
        LCS1.append(list(word1)[L])
        # print("LCS1:",LCS1)
        dfs1(word1, word2,L+1,LCS1)
        dfs1(word1, word2,L+1,LCS)

dfs1(first,second,0,LCS)
print(ans)
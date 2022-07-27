alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet.insert(0,0)
word = list(input())
# word  = list(map(int,word))
N = len(word)

ans = []
def dfs(L,onetwo,possible):
    global ans
    if L > N:
        return
    elif onetwo == 1 and int(word[L-1]) < 27:
        possible.append(alphabet[int(word[L-1])])        
    elif onetwo == 2 and int("".join(word[L-2:L])) < 27:
        possible.append(alphabet[int("".join(word[L-2:L]))]) 
    if L == N:
        ans.append("".join(possible))
        return
    if possible:
        possible.pop()
    dfs(L+1,1,possible)
    if possible:
        possible.pop()
    dfs(L+2,2,possible)
    

    
dfs(0,0,[])

print(ans)

def change(num):
    n = num // 2
    l = num % 2
    if n > 0 :
        change(n)
    
    print(l,end = '')


change(int(input()))

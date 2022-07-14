import time
start_time = time.process_time()

need = list(input())
n = int(input())
for _ in range(n):
    cls = list(input())
    while cls:
        now = cls.pop(0) 
        if now in need:
            if now != need.pop(0):
                print("NO")
                break
    else:
        if len(need) == 0:
            print("YES")
        else:
            print("NO")

end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")
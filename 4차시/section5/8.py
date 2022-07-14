import time
start_time = time.process_time()
n = int(input())

note ={input():0 for _ in range(n)}
p = [input() for _ in range(n-1)]

print(set(note)-set(p))


end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")
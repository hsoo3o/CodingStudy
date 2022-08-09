# Baekjoon 14888

from sys import stdin
from collections import deque
import sys
from itertools import permutations

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
sign_counts = list(map(int, stdin.readline().split()))
sign_ = []
ans_min = 1e12
ans_max = -1e12
for i in range(sign_counts[0]):
    sign_.append("+")
for i in range(sign_counts[1]):
    sign_.append("-")
for i in range(sign_counts[2]):
    sign_.append("x")
for i in range(sign_counts[3]):
    sign_.append("/")

sign = list(set((permutations(sign_))))

for s in sign:
    result = nums[0]
    for i in range(len(s)):
        if s[i] == "+":
            result += nums[i+1]
        elif s[i] == "-":
            result -= nums[i+1]
        elif s[i] == "x":
            result *= nums[i+1]
        elif s[i] == "/":
            result /= nums[i+1]
            result = int(result)
                
    ans_min = result if result < ans_min else ans_min
    ans_max = result if result > ans_max else ans_max

print(ans_max)
print(ans_min)
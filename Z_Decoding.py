
from collections import deque

n = int(input())
s = input()

ans = deque()

for ch in reversed(s):
    ans.insert(len(ans) // 2, ch)

print(''.join(ans))

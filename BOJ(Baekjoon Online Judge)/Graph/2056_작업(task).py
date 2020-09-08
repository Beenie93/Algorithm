#https://www.acmicpc.net/problem/2056

import sys, heapq
from collections import deque

n = int(sys.stdin.readline())

a = [[]*(n+1) for _ in range(n+1)]
d = [0] * (n+1)
ind = [0] * (n+1)
work = [0] * (n+1)

for i in range(1,n+1):
    info = list(map(int,sys.stdin.readline().split()))
    if len(info) > 2:
        for k in info[2:]:
            a[k].append(i)
            ind[i] += 1
    work[i] = info[0]

q = deque()

for i in range(1,n+1):
    if ind[i] == 0:
        q.append(i)
        d[i] = work[i]

while q:
    x = q.popleft()
    for k in a[x]:
        ind[k] -= 1
        if d[k] < d[x]+work[k]:
            d[k] = d[x]+work[k]
        if ind[k] == 0:
            q.append(k)
ans = 0

for i in range(1,n+1):
    if ans < d[i]:
        ans = d[i]
print(ans)

"""
n = int(sys.stdin.readline())

a = [[] for _ in range(n+1)]
ind = [0] * (n+1)
d = [0] * (n+1)
ans = [0] * (n+1)

for i in range(1,n+1):
    t, m, *temp = map(int,sys.stdin.readline().split())
    d[i] = t
    for j in range(m):
        a[i].append(temp[j])
        ind[temp[j]] += 1

q = deque()

for i in range(1,n+1):
    if ind[i] == 0:
        q.append(i)
        ans[i] = d[i]

while q:
    x = q.popleft()
    for y in a[x]:
        ind[y] -= 1
        ans[y] = max(ans[y], ans[x] + d[y])
        if ind[y] == 0:
            q.append(y)

print(max(ans))
"""
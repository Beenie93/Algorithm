#https://www.acmicpc.net/problem/1697

import sys
from collections import deque

MAX = 200000 # 또는 MAX = max(n,k)*2
n, k = map(int,sys.stdin.readline().strip().split())
check = [False] * (MAX+1)
d = [-1] * (MAX+1)

def bfs(start):
    q = deque()
    check[start] = True
    q.append(start)
    d[start] = 0

    while q:
        x = q.popleft()
        for next in [x+1,x-1,x*2]:
            if 0 <= next <= MAX and check[next] == False:
                check[next] = True
                q.append(next)
                d[next] = d[x] + 1
bfs(n)
print(d[k])
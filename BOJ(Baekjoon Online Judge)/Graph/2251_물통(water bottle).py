#https://www.acmicpc.net/problem/2251

import sys
from collections import deque

a, b, c = map(int,sys.stdin.readline().split())
visit = [[False] * (201) for i in range(201)]
v = []

q = deque()
q.append((0,0,c))

while q:
    x,y,z = q.popleft()
    if visit[x][y]:
        continue

    visit[x][y] = True

    if x == 0:
        v.append(z)

    if x+y > b:
        q.append((x+y-b,b,z))
    else:
        q.append((0,x+y,z))

    if x+z > c:
        q.append((x+z-c,y,c))
    else:
        q.append((0,y,x+z))

    if y+x > a:
        q.append((a,y+x-a,z))
    else:
        q.append((y+x,0,z))

    if y+z > c:
        q.append((x,y+z-c,c))
    else:
        q.append((x,0,y+z))

    if z+x > a:
        q.append((a,y,z+x-a))
    else:
        q.append((z+x,y,0))

    if z+y > b:
        q.append((x,b,z+y-b))
    else:
        q.append((x,z+y,0))

v.sort()
print(" ".join(map(str,v)))
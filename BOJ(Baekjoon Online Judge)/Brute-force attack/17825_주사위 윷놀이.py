#https://www.acmicpc.net/problem/17825

import sys

n = list(map(int,sys.stdin.readline().split()))
d = [(1,2),(1,4),(1,6),(1,8),(2,10)
    ,(1,12),(1,14),(1,16),(1,18),(3,20)
    ,(1,22),(1,24),(1,26),(1,28),(4,30)
    ,(1,32),(1,34),(1,36),(1,38),(1,40),(21,0)]
d1 = [(2,13),(,16),(1,19),(2,25)]
d2 = [(1,22),(1,124),(2,25)]
d3 = [(1,28),(1,27),(1,26),(2,25)]
d4 = [(1,30),(1,35),(1,40),(1,0)]

sum = 0
k=0
for i in n:
    last = 0
    for j in range(i):
        sum += d[j+k][1]
    if d[j+k][0] == 2:


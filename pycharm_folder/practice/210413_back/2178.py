# https://www.acmicpc.net/problem/2178

# 4 6
# 101111
# 101010
# 101011
# 111011
#
# 15

import sys

n,m = map(int, sys.stdin.readline().split())

print(n,m)

data_list = []
for i in range(n):
    data_list.append(list(map(int,input())))

print(data_list)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0

def dfs(x,y):
    global count
    print(x,y)
    if x < 0 or x >= m - 1 or y < 0 or y >= n - 1:
        return
    if data_list[x][y] == 0:
        return
    if data_list[x][y] == 1:
        count += 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

dfs(0,0)
print(count)





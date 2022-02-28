import sys
sys.setrecursionlimit(5000)

ver = [-1,1,0,0]  # 상 하 좌 우 x좌표
hor = [0,0,-1,1]  # 상 하 좌 우 y좌표

def search(x,y):
  v[x][y] = 1 # 방문

  for i in range(4):
    tx = x+ver[i]
    ty = y+hor[i]

    if 0 <= tx < n and 0 <= ty < m: # x좌표의 값, y좌표의 값이 범위 내에 있는 경우
      if v[tx][ty]==0 and f[tx][ty]==1: # 방문이력이 없고 배추가 있는 경우
        search(tx,ty)

T = int(input())  # 테스트케이스 수
count = [0 for _ in range(T)] # 지렁이의 수 카운트

# 입력 받아서 초기화
for i in range(T):  # 테스트케이스 수 만큼 반복
  t = list(map(int, input().split()))
  m, n, k = t[0],t[1],t[2]  # 각 가로, 세로, 배추개수 
  f = [[0 for _ in range(m)] for _ in range(n)]
  for j in range(k):  # 배추의 개수만큼 반복
    po = list(map(int, input().split()))  # 배추가 심어진 위치
    f[po[1]][po[0]] = 1 # 해당 위치에 배추가 있다는 의미
  v = [[0 for _ in range(m)] for _ in range(n)] # 해당 위치 방문 여부

  for x in range(n):
    for y in range(m):
      if f[x][y]==1 and v[x][y]==0:  # 배추가 있고 방문한 적이 없는 경우
        count[i] += 1
        search(x,y)


for i in range(T):
  print(count[i])

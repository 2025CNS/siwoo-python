h,w=map(int,input().split())
n=int(input())
grid=[[0]*w for _ in range(h)]#grid 값을 h*w크기의 격잪판을 0으로 초기화 한 값 저장
for _ in range(n):#n-1번 반복
    l,d,x,y=map(int,input().split())#길이 방향 좌표 입력
    x-=1
    y-=1 #x,y에 -1만큼 한 값만큼을 저장
    if d==0:
        for i in range(l):#l-1번 반복
            grid[x][y+i]=1 #grid[x][y+j]에 1 저장(가로방향)
    else:
        for i in range(l):
            grid[x + i][y] = 1#세로방향
for row in grid:
    print(" ".join(map(str, row))) #격자판 출력           

        
            
            
            
            
    
    
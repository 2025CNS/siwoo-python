array=[]
for i in range(10):  
    array.append(list(map(int,input().split())))#array 리스트로 입력받음

x,y=1,1

while True:
    if array[x][y]==0:#만약 현재칸이 0이라면 9로 변환시키기
        array[x][y]=9
    elif array[x][y]==2:#현재칸이 2(먹이)라면 9로 바꿔주고 반복 종료
        array[x][y]=9
        break
    if array[x][y+1]==1 and array[x+1][y]==1:#오른쪽과 아래 모두 1(벽)이라면 종료
        break
    if array[x][y+1]!=1:#오른쪽이 1(벽)이  아니라면 y를 증가 시키기
        y+=1
    elif array[x+1][y]!=1:#아래쪽이 1(벽)이 아니라면 x를 증가시키기
        x+=1
for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()#10*10판출력하기
                
            
    
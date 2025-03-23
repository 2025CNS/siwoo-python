d=[]#빈리스트 생성
for i in range(20):#20번 반복
    d.append([])#리스트 안의 리스트
    for j in range(20):#20 번 반복
        d[i].append(0)#이중 리스트에 0 추가
n=int(input())
for i in range(n): #n번 반복
    x,y=input().split()#xy입력
    d[int(x)][int(y)]=1
for i in range(1,20):
    for j in range(1,20):#가로 19, 세로 19
        print(d[i][j],end=' ')#공백두고 한 줄로 0과 1 출력
    print()
        


d=[]

for i in range(19):#19번 반복
    d.append([])#중복 리스트 생성
    for j in range(19):
        d[i].append(0)#d[i]에 0추가

for i in range(19):
    d[i]=list(map(int,input().split()))# 바둑판 입력
    
n=int(input())

for i in range(n):#n번 반복하기
    x,y=map(int,input().split())#x,y 값 입력
    for j in range(19):
        if d[x-1][j]==0:
            d[x-1][j]=1#만약 가로가 0이면 1 저장
        else:
            d[x-1][j]=0#아니면 0 저장하기
        if d[j][y-1]==0:
            d[j][y-1]=1
        else:
            d[j][y-1]=0 #세로에 저장
            
for i in range(19): #19번 반복
    for j in range(19):
        print(d[i][j], end=' ')#줄 비꿈 없이 출력하기
    print()    
        
        
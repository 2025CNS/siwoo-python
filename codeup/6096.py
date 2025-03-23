n=int(input())
d = [[0 for _ in range(19)] for _ in range(19)]
for i in range(n):#n번 반복하기
    x,y=input().split()
    x -= 1  # 1-based에서 0-based로 변환
    y -= 1  # 1-based에서 0-based로 변환
    for j in range(1,20):#1부터 19까지 반복
        if d[j][int(y)]==0:
            d[j][int(y)]=1#만약 d[j][int[y]]의 값이 0이라면 이 값에 1을 저장
        else:
            d[j][int(y)]=0#아니면 0 저장
        if d[int(x)][j]==0:
            d[int(x)][j]=1#만약 d[int(x)][j]의 값이 0이라면 1 저장
        else:
            d[int(x)][j]=0#아니면 0 저장
for i in range(19):
    print(' '.join(map(str, d[i])))
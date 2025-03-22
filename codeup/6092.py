n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])#a에 저장된 값 정수로 변환
d=[]#d라는 이름의 빈 리스트 생성
for i in range(24):#0~23까지 24번 반복
    d.append(0)
for i in range(n): #n-1번 반복하기
    d[a[i]]+=1#번호를 부르면 그 번호의 카운트 1 증가
for i in range(1,24):#1~23까지 반복
    print(d[i],end=" ")#불린 횟수 출력   
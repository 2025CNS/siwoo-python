a,b,c=map(int,input().split())
d=1#d에다 1을 저장해라
while d%a!=0 or d%b!=0 or d%c!=0 :#날 수가 방문주기 a또는 b또는 c와 나누어떨어지지 않는동안
  d += 1#d에다 d+1을 한 값을 더해라
print(d)#d를 출력

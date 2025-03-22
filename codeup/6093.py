n=int(input())
a=input().split()
for i in range(n-1, -1, -1) :#n-1에서 0까지 -1먼큼 줄이며 반복
  print(a[i], end=' ')#a의 i에 해당값을 출력

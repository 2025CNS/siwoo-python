A,B=map(int,input().split())
C=int(input())
A=A*60
min=A+B+C
A=(min//60)%24
B=min%60
print(A,B)
  
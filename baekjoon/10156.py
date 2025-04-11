#10156. 과자
K,N,M=map(int,input().split())
R=K*N-M
if R<=0:
    print(0)
else:
    print(R)

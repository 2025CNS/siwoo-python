T=int(input())
for i in range(T):
    A,B=input().split()
    A=int(A)
    L=len(B)
    R=''    
    for j in range(L):
        R+=B[j]*A 
    print(R)
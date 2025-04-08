#1789.소인수분해
N=int(input())
def prime_factorization(n):
    fac=[]
    for i in range(2,n+1):
        while n%i==0:
            fac.append(i)
            n=n//i
    return fac
result=prime_factorization(N)
for i in range(len(result)):
    print(result[i], end=' ')
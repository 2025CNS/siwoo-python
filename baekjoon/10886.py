#10886.0=not cute, 1=cute
N=int(input())
li=[]
for i in range(N):
    li.append(int(input()))
a=li.count(0)
b=li.count(1)
if a>b:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
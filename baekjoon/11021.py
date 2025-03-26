T=int(input())
i=0
while True:
    i+=1
    if i<=T:
        A,B=map(int,input().split())
        print(f'Case #{i}: {A+B}')
    else:
        break
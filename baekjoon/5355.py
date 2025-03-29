T=int(input())
for i in range(T):
    N=input().split()
    a=float(N[0])
    for j in range(len(N)):
        if N[j] =='@':
            a=a*3
        elif N[j] =='%':
            a=a+5
        elif N[j] =='#':
            a=a-7
    print(f'{a :.2f}')
        
        
    
    

w,h,b=map(int,input().split())
pixel=w*h*b/8/1024/1024
i=f"{pixel:.2f}"
print(f"{i} MB")
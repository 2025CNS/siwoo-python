# 10988. 팰린드롬인지 확인하기
v=list(input())
if v==v[::-1]:
    print(1)
else:
    print(0)
a=int(input("请输入几个"))
b=int(2)
count=int(0)
c=a
while b<=c:
    c=a
    while a!=0:
        a=a/b
        count+=b
    print(f"{b}分法用{count}次")
    a=c
    count=0
    b=b+1


    
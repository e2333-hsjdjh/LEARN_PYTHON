from random import randint
count=1
i=int(input("请输入你想猜从1-几"))
right_number=int(randint(int(1),int(i)))
user_number_2=int(i/2)
user_number_1=int(1)
user_number_3=int(i)
while right_number!=user_number_2:
    print(f"这是第{count}次")
    if user_number_2<right_number:
        print("猜小了")
        user_number_1=user_number_2
        user_number_2=(user_number_1+user_number_3)/2
    elif user_number_2>right_number:
        print("猜大了")
        user_number_3=user_number_2
        user_number_2=(user_number_1+user_number_3)/2
    count+=1
else:
    print(f"花了{count}次，你成功了")
    
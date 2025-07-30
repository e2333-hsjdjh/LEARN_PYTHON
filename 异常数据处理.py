#异常数据的处理
#语法错误（SyntaxError）: 代码中存在语法错误，Python无法解析。
#运行时错误（RuntimeError）: 代码在运行时发生错误，例如除以零。
#逻辑错误（LogicError）: 代码运行时没有报错，但结果不



try:
    rea_fund=float(input("请输入您现在卡里的余额"))
    Ori_fund=float(input("请输入充值金额"))
except Exception as e:  # 捕获特定的异常类型   #可以出现错误类型，也可以不跟，及所有错误都会执行
    print(f"输入错误，请输入数字: {e}")
    exit()


flag=int(1)
if rea_fund!=0:
    flag=0
if Ori_fund<1000:
    rea_fund+=Ori_fund
elif Ori_fund>=1000 and Ori_fund<2000:
    rea_fund+=Ori_fund*1.15
elif Ori_fund>=2000 and Ori_fund<5000:
    rea_fund+=Ori_fund*1.18
elif Ori_fund>=5000 and Ori_fund<10000:
    rea_fund+=Ori_fund*1.2+500
else:
    rea_fund+=Ori_fund+10000
if flag==1:
    print(f"您是新用户，本次充值共{rea_fund}元，可享受首充福利")
    rea_fund+=0.1*rea_fund
print(f"您的卡里还有{rea_fund}元")
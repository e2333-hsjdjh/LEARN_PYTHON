#抛出异常

#raise Exception("这是一个异rewt常")

def funa():
    print("gfdhgf")
    raise Exception("这是一个异常")
funa()



try:
    funa()
except Exception as e:
    print("捕获到异常:", e)

print("程序继续执行")
#捕获异常，程序继续往下进行
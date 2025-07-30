word="汉字"
for letter in word:
    print(letter)
print("遍历结束")
print(letter)


for i in range(1,101,10):
    print(i)



for j in range(1,10):
    for p in range(1,j+1):
        print(f"{p}*{j}={j*p}",end="\t")
    print()


from time import sleep
for i_1 in range(0,51):
    print(f"{'_'*i}{'-'*(50-1)}",end="\r") 
    sleep(0.1)
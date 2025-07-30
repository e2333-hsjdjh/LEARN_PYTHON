from progressbar import progressbar

my_list=["早晨","晚上","中午","下午 "]
print(my_list[0])
print(my_list[1])   
print(my_list[0:2])  #输出前两个元素
print(my_list.index("早晨"))  #输出元素"早晨"的索引
print(my_list.count("早晨"))  #输出元素"早晨"的个数 
my_list.append("夜晚")  #在列表末尾添加元素
my_list.insert(0,"清晨")  #在列表开头添加元素   
print(my_list)  #输出列表
print(len(my_list))  #输出列表长度
my_list.insert(2,"清晨")  #在列表的第三个位置插入元素"清晨"

my_list.remove("早晨")  #删除列表中的元素"早晨"
my_list.pop(0)  #删除列表中的第一个元素




list_2=["清晨","夜晚"]
selist=["早晨","晚上","中午","下午 ","夜晚","清晨",list_2]
selist[-1]=["早晨","晚上","中午","下午 ","夜晚","清晨"]  #将列表的最后一个元素替换为另一个列表
print(selist)  #输出列表

print(my_list+list_2)  #将两个列表合并

print(selist[-1][0])  #输出列表最后一个元素的第一个元素



for i in range(len(my_list)):
    print(my_list[i])  #遍历列表并输出每个元素


test_list=[print("hfudshu"),print(),progressbar(0.1)]  #创建一个列表，其中包含打印语句和进度条函数
# 注意：print()函数在列表定义时会被执行，因此会输出空行
#在定义时，内部函数已经被执行

#清除列表的三种方式
my_list.clear()  #清除列表中的所有元素
del my_list  #删除整个列表  
my_list=["早晨","晚上","中午","下午 "]  #重新定义一个列表
my_list=[]  #将列表清空
#注意：清空列表和删除列表是不同的操作，清空列表后仍然可以使用该变量名，而删除列表后该变量名将不再存在
#使用列表推导式创建一个新列表
new_list = [x for x in my_list if x != "早晨"]  #创建一个新列表，包含my_list中不等于"早晨"的元素
print(new_list)  #输出新列表
my_list=['1','2','3','4','5']  
#用for循环删除列表
for item in range(len(my_list)):  #遍历my_list的副本
    my_list.pop()  #删除该元素

my_list=['1','2','3','4','5']
print()
print(sorted(my_list,reverse=True))  #输出my_list的逆序排序
print(sorted(my_list))  #输出my_list的正序排序











# 创建一个3x3的二维列表，初始值为0
matrix = [[0 for _ in range(3)] for _ in range(3)]


matrix[0][1] = 5      # 修改第1行第2列的值为5
print(matrix[0][1])   # 访问第1行第2列的值

n = int(input("请输入矩阵大小:"))
matrix = []
for i in range(n):
    row = input(f"请输入第{i+1}行（用空格分隔）: ").split()
    matrix.append([int(x) for x in row])
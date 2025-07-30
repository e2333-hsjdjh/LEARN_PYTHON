#字符串
#字符串相关的函数
print(ord('2')) #用来查询某一个字符的ascII值
print(chr(39))  #用来将某个ascII值转化为字符
"""
转义符
\\反斜杠
\'引号
\tTab键
\n换行
\a铃响
\b退后一格
\r游标返回
"""

#字符串的拼接
print("whelcome to "+' shanxi')
print('nihao'*10)
message='''
    昨夜西风凋碧树
        独上高楼，望尽天涯路
'''
print(message)

#函数索引
name='michelle'
for i in name:
    print(i)
print("print successfully")
print(type(name))
for i in enumerate(name):
    print(i)  #enumerate函数可以将字符串的索引和字符一起输出
#字符串的切片
print(name[3:])   #输出第四个字符到最后
print(name[:3])   #输出前三个字符
print(name[-1])   #输出最后一个字符
print(name[-3:])  #输出最后三个字符
#字符串的长度
print(len(name))  #输出字符串的长度
#字符串的遍历
for i in range(len(name)):
    print(name[i])  #输出每个字符
#字符串的查找
print(name.find('c'))  #查找字符c的位置
print(name.index('c'))  #查找字符c的位置，如果不存在会报错


my_name='John Doe , hello world'
#字符串不可修改
my_name = my_name.replace('John', 'Jane')
print(my_name)  # 输出: Jane Doe
# 重新赋值给变量
my_name = my_name + ' Smith'

print(my_name)  # 输出: Jane Doe Smith
# 使用字符串格式化
formatted_name = f"Hello, {my_name}!"
print(formatted_name)  # 输出: Hello, Jane Doe Smith!

print("The length of my name is:", len(my_name))  # 输出: The length of my name is: 20
# 使用字符串切片
first_name = my_name[:4]  # 获取前四个字符
print("First name:", first_name)  # 输出: First name: Jane  
# 使用字符串拼接
last_name = my_name[5:]  # 获取从第五个字符开始到结尾的字符串
print("Last name:", last_name)  # 输出: Last name: Doe Smith    
# 使用字符串分割
name_parts = my_name.split(' ')  # 按空格分割字符串
print("Name parts:", name_parts)  # 输出: Name parts: ['Jane', 'Doe', 'Smith']
# 使用字符串连接
joined_name = ' '.join(name_parts)  # 将列表中的字符串连接成一个字符串
print("Joined name:", joined_name)  # 输出: Joined name: Jane Doe Smith
# 使用字符串查找
index_of_doe = my_name.find('Doe')  # 查找子字符串 'Doe' 的索引
print("Index of 'Doe':", index_of_doe)  # 输出: Index of 'Doe': 5



new='1111335427653'
new = new.replace('11', '2',4)  # 替换前四个 '11' 为 '2'
print(new)  # 输出: 222335427653


my_new_name=my_name.split(' ')  # 按空格分割字符串
print(my_new_name)  # 输出: ['Jane', 'Doe', 'Smith']

print((',').join(my_new_name))  # 使用逗号连接列表中的字符串
# 输出: Jane,Doe,Smith



my_name_new=my_name.strip('h') # 去除字符串两端的 'h'
print(my_name_new)  # 输出: Jane Doe Smit

print(my_name[7:0:-1]) # 输出: eoD enaJ，字符串切片从第七个字符到第一个字符（逆序）
print(my_name[::-1])  # 输出: !htimS eoD enaJ，字符串逆序输出
print(my_name[7:0:-2])  # 输出: eD aJ，字符串切片从第七个字符到第一个字符（逆序，每隔一个字符输出）
print(my_name[7:0:-3])  # 输出: eJ，字符串切片从第七个字符到第一个字符（逆序，每隔两个字符输出）
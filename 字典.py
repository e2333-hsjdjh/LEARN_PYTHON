my_dict={
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
}
print(my_dict)

my_dict_2={
    '张三': 18,
    '李四': 20,
    '王五': 22,
    '赵六': 25,
    '钱七': 30,
    '孙八': 28,
    '周九': 26,
    '吴十': 24,
    '郑十一': 29,
    '冯十二': 27,
    '陈十三': 23,
}

print(my_dict_2['孙八'])

#字典直接用key找到他的value

my_dict_3={
    '张三':{
        "总分": 500,
        "语文": 90,
        "数学": 95,
        "英语": 85,
        "物理": 80,
        "化学": 75,
        "生物": 70,
        '志愿表': ['计算机科学', '电子工程', '机械工程'],
    },
    '李四':{
        "总分": 480,
        "语文": 85,
        "数学": 90,
        "英语": 80,
        "物理": 75,
        "化学": 70,
        "生物": 65,
        '志愿表': ['土木工程', '环境科学', '材料科学'],
    },
}

print(my_dict_3['张三']['志愿表'][0])


#key是唯一的

#若key一样后面的会覆盖前面的

#删除指定键值对
del my_dict_2['张三']  # 删除键为'张三'的元素
print(my_dict_2)  # 输出: {}
#删除指定元素
my_dict_2.pop('李四')  # 删除键为'李四'的元素
print(my_dict_2) 
#删除所有元素
my_dict_2.clear()  # 清空字典
print(my_dict_2)  # 输出: {}
#删除字典
del my_dict_2  # 删除整个字典
# print(my_dict_2)  # 会报错，因为字典已被删除

#复制字典
my_dict_2=my_dict_3.copy()  # 复制字典
#获取字典的元素个数
print(len(my_dict_2))  # 输出: 0，字典为空


for key, value in my_dict_2.items():  # 遍历字典
    print(f"Key: {key}, Value: {value}")  # 输出键和值
for key in my_dict_2:  # 遍历字典的键
    print(f"Key: {key}")  # 输出键
for value in my_dict_2.values():  # 遍历字典的值
    print(f"Value: {value}")  # 输出值

print()
print(max(my_dict_2))

print()

print('apple'>'Apple')  # 字符串比较，输出: True，因为 'a' 的 ASCII 值大于 'A'
print('electronic'>'electric')  # 字符串比较，输出: True，因为 'o' 的 ASCII 值大于 'i'
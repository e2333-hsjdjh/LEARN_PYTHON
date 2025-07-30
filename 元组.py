the_tuple=(1, 2, 3, 4, 5)



#元组不可变




print(the_tuple[0])  # 输出第一个元素
print(the_tuple[1:3])  # 输出第二个到第三个元素
# 元组的长度
print(len(the_tuple))  # 输出5
# 元组的连接
another_tuple = (6, 7, 8)
new_tuple = the_tuple + another_tuple
print(new_tuple)  # 输出(1, 2, 3, 4,
# 5, 6, 7, 8)

# 元组的重复
repeated_tuple = the_tuple * 2      
print(repeated_tuple)  # 输出(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# 元组的成员测试
print(3 in the_tuple)  # 输出True
print(10 in the_tuple)  # 输出False

# 元组的遍历
for item in the_tuple:
    print(item, end=' ')  # 输出1 2 3 4 5
print()  # 换行

# 元组的索引和切片
print(the_tuple.index(3))  # 输出2，3在元组中的索引
print(the_tuple[1:4])  # 输出(2, 3, 4)，切片从索引1到索引3（不包括4）
# 元组的最大值和最小值
print(max(the_tuple))  # 输出5，元组中的最大值
print(min(the_tuple))  # 输出1，元组中的最小值
# 元组的排序（需要转换为列表）
sorted_tuple = sorted(the_tuple)
print(sorted_tuple)  # 输出[1, 2, 3, 4, 5]，排序后的列表
# 元组的转换
list_from_tuple = list(the_tuple)
print(list_from_tuple)  # 输出[1, 2, 3, 4, 5]，转换后的列表
# 元组的哈希值
print(hash(the_tuple))  # 输出元组的哈希值
# 元组的比较
another_tuple2 = (1, 2, 3, 4, 5)
print(the_tuple == another_tuple2)  # 输出True，两个元组相等
print(the_tuple < another_tuple2)  # 输出False，比较元组的大小
# 元组的解包
a, b, c, d, e = the_tuple
print(a, b, c, d, e)  # 输出1 2 3 4 5，解包后的值
# 元组的嵌套
nested_tuple = (the_tuple, another_tuple)
print(nested_tuple)  # 输出((1, 2, 3, 4, 5), (6, 7, 8))，嵌套的元组
# 元组的生成器表达式
generator_tuple = tuple(x * 2 for x in the_tuple)
print(generator_tuple)  # 输出(2, 4, 6, 8, 10)，生成器表达式生成的元组
# 元组的函数应用    
def apply_function_to_tuple(func, tup):
    return tuple(func(x) for x in tup)
result_tuple = apply_function_to_tuple(lambda x: x ** 2, the_tuple)
print(result_tuple)  # 输出(1, 4, 9, 16, 25)，应用函数后的元组
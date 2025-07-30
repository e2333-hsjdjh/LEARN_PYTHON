# 正则表达式：
# 记录文本规则的代码
# 字符串处理工具
# 语法比较复杂，可读性较差
# 但通用性很强，可以用多个不同语言

import re
# re.match(pattern=,string=,flags=)#三个参数分别是要匹配的正则表达式，  要匹配的字符串
a='豪'
b='豪法gfvdhcsaukjfhdaskhfadsk'

res_1=re.match(a,b)
print(res_1.group())  #match从开头开始匹配

a='豪'
b='豪法gfvdhcsaukjfhdaskhfadsk'

res_2=re.match('豪哈哈哈',b)
print(res_2.group())  
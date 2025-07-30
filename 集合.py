my_set={'my','name','is','not','important'}
print(my_set)
my_set.add('important') # Adding an element to the set
print(my_set)   

#并集
my_set2={'my','name','is','important'}
print(my_set.union(my_set2)) # Using union method to combine sets
my_set3=my_set | my_set2 # Using the pipe operator to combine sets
print(my_set3)
#交集
print(my_set.intersection(my_set2)) # Using intersection method to find common elements
print(my_set & my_set2) # Using the ampersand operator to find common elements
#差集
print(my_set.difference(my_set2)) # Using difference method to find elements in my_set not in my_set2
print(my_set - my_set2) # Using the minus operator to find elements in my_set not in my_set2

for item in my_set: # Iterating through the set
    print(item)




#集合最多的用处就是去重

set1={1,2,3}
set2={3,4,5}
set3=set1.union(set2) # Using union method to combine sets  
print(set3)  # 输出: {1, 2, 3, 4, 5}

my_list=[1,2,3,4,5,1,2,3]
my_set_from_list=set(my_list)  # Converting list to set to remove duplicates
print(my_set_from_list)  # 输出: {1, 2, 3, 4, 5}

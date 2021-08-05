"""
Take a list of numbers. Take the odd numbers and convert them into a dictionary with the number as the key and their position in the list as value
"""

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
len_num_list = len(num_list)

newdct={}
lst=[]
for i in range(len_num_list):
    if num_list[i] % 2 != 0:
        lst.append(num_list[i])
        lst.append(i)
        
items = iter(lst)
newdct = dict(zip(items, items))
print(newdct)

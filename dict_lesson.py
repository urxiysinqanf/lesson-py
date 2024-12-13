# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
#

#
# my_dict = {'name': 'Alice', 'age': 25}
# # my_dict['city'] = 'New York'        # {'name': 'Alice', 'age': 25, 'city': 'New York'}
# my_dict.update({'age': 26, 'job': 'Engineer'})  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
# print(my_dict)
#
# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# age = my_dict.pop('age1')  # 25
# city = my_dict.pop('city1', 'Not Found')  # 'New York'
# print(city)
# my_dict.clear()  # {}
# print(my_dict)
#
# my_dict = {'name': 'Alice', 'age': 25}
# name = my_dict['name']  # 'Alice'
# age = my_dict.get('age1', 0)  # 25
# print(age)
# city = my_dict.get('city', 'Unknown')  # 'Unknown'
#
# my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# for key, value in my_dict.items():
#     print(f'Key: {key}, Value: {value}')
# # Output:
# # Key: name, Value: Alice
# # Key: age, Value: 25
# # Key: city, Value: New York
#
# for key in my_dict.keys():
#     print(f'Key: {key}')
# # Output:
# # Key: name
# # Key: age
# # Key: city
#
# for value in my_dict:
#     print(f'Value: {value}')
# # Output:
# # Value: Alice
# # Value: 25
# # Value: New York
#
# filtered_dict = {key: value for key, value in my_dict.items() if isinstance(value, int)}
# print(filtered_dict)  # {'age': 25}
#
# Увеличение возраста на 1 год
# for key in my_dict:
#    print(my_dict[key])
#    if key == 'age':
#        my_dict[key] += 1
# print(my_dict)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# my_dict = {"name": "John", "age": 30, "city": "New York", "salary": 50000}
# for key in my_dict:
#  if key == "age":
#    my_dict[key] += 1
# print(my_dict)


# Изначальный словарь
# original_dict = {'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit'}

# Обратный словарь
# reverse_dict = {'fruit': 'banana', 'vegetable': 'carrot'}



text = input(f"Введите текст: ")

# понятия не имею почему пришлось всем подряд чистить эти долбанные знаки, но по другому они все не убирались

import string
table = str.maketrans("", "", string.punctuation)
text = text.translate(table)

text = text.replace("“", "")
text = text.replace("‘", "")
text = text.replace("’", "")
text = text.replace("”", "")
text = text.strip()
text = text.lower()
words_list = text.split()


super_dict = {}
for i in words_list:
    if i in super_dict:
        super_dict[i] += 1
    else:
        super_dict[i] = 1

print(super_dict)
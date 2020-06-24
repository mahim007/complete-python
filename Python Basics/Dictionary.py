my_dict = {
    'a': [1, 2, 3, 4],
    'x': 'hello world',
    'c': True,
    'age': 22
}

copy_dict = my_dict.copy()
my_dict.pop('age')
my_dict.update({"email": "mahim@gmail.com"})
my_dict.update({'c': False})

print(my_dict)
print(copy_dict)

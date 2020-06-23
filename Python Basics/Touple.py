my_touple = (1,2,3,4,5,3)
print(my_touple)
print(my_touple.index(3))

print(my_touple.count(3))

name = 100
my_data = {
    name: 'mahim',
    'age': 25,
    True: [1,2,3],
    (1,2,3): (1,2,3,4,5)
}

print(my_data[(1,2,3)][0:3])

new_touple = my_touple
x,y,z,*others = new_touple
print(x, y, z)
print(others)
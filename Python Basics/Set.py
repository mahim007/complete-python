my_set = {1,2,3,4,5}
print(my_set)

another_set = my_set.copy()
another_set.add(100)
print(another_set)
print('my_set: ', my_set)
another_set.clear()
print("another_ser clear: ", another_set)
my_set.add(5)
print(my_set)

my_list = [1,2,3,4,4,5,5,6,6,]
print(my_list)
my_set2 = set(my_list)
print(my_set2)
final_list = list(my_set2)
print(final_list)
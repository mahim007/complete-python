def highest_even(my_list):
    max_even = 0
    for item in my_list:
        if item % 2 == 0:
            max_even = max(max_even, item)
    return max_even


result = highest_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 123, 234, 345])
print(result)

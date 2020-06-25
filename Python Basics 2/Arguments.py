def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(sum(args))


print(my_func(1,2,3,4,5, name = 'mahim', age = 25))

# print(sum(1,2))
print(sum([1,2,3]))
print(sum((1,2,3)))
print(sum((1,2,3)))

#Rule: params, *args, default parameters, **kwargs
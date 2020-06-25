total = 0


def parent():
    total = 100

    def func():
    #    nonlocal total
        global total
        # total1 = total+1
        #total = total1
        total += 1
        return total

    return func

my_func = parent()
print(my_func())
print(my_func())

print(total)

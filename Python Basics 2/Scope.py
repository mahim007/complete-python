a=1

def parent():
    # a = 10
    def child():
        # a = 5
        print(a)
        print(sum)
    child()


print(a)
parent()
print(a)

#Rule: 1 -> start with local
# 2-> parent local
# 3 -> global
# 4 -> built-in python function 
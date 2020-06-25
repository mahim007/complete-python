def do_sum(num1, num2):
    '''
    Info: this function returns another function!!!
    '''
    n1 = num1 + 1
    n2 = num2 + 1

    def do_another_thing():
        '''
        another function just multiplies!
        '''
        return n1*n2
    return do_another_thing


do_calculate = do_sum(10, 5)
print(do_calculate())

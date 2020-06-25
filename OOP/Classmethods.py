class MyClass:
    name = 'mahim'

    def __init__(self, result):
        super().__init__()
        self.result = result

    @classmethod
    def adding(cls, num1, num2):
        print(cls.name)
        return cls(num1 + num2)
    
    @staticmethod
    def find_square(num):
        return num**2


example = MyClass.adding(2, 3)
print(example.result)


print(MyClass.find_square(3))
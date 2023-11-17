import random
class Skritoe:

    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def __result(self):
        return self.__num1 + self.__num2
    def get(self):
        return self.__result()

numbers = Skritoe(4, 6)
print(numbers.get())

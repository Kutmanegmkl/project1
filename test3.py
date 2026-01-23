# class CandyBox:
#     def __init__(self,candies):
#         self.candies=candies
#     def get_candies(self):
#         return self.candies
#     def set_candies(self, value):
#         if value<0:
#             print("Нельзя, конфет не может быть меньше нулья!")
#             return 
#         self.get_candies=value

# box=CandyBox(10)

# box.set_candies(5)
# box.set_candies(-3)

# class Box:
#     def __init__(self):
#         self._weight=10

#     @property 
#     def weight(self):
#         return self._weight

# box=Box()
# print(box.weight)

# class Animal:
#     def speak(self):
#         print("Животное ихдает звук")

# class Dog(Animal):
#     def speak(self):
#         print("Гав")

# class Cat(Animal):
#     def speak(self):
#         print("Мяу")

# animals = [Dog(), Cat(), Animal()]

# for a in animals:
#     a.speak()


class Dog():
    def speak(self):
        print("Gav")

class Robot:
    def speak(self):
        print("biip")
things=[Dog(), Robot()]


for i in things:
    i.speak()   
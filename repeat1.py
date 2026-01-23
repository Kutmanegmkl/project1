


# def read_file(path):
#     list_=list()
#     with open(path,'r', encoding="utf-8") as file:
#         for line in file:
#             list_.append(line)

#     return list_


# print(read_file("client.txt"))


# def add(a,b=8):
#     return a+b

# print(add(5,6))
# print(add(5))


# def show_args(*args):
#     print(args)

# show_args(1,2,3,4,5,6,7,8,9)


# def sum_number(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total

# print(sum_number(1,2,32,234,234))


# def show_kwargs(**kwargs):
#     print(kwargs)

# print(show_kwargs(name='Aijan', age=28,city='Bishkek'))

# def log_event(**data):
#     for key,value in data.items():
#         print(f"{key}:{value}")

# log_event(user="Kutman", action='login', status="ok")


# def demo(*args, **kwargs):
#     print("args", args)
#     print("kwargs", kwargs)

# print(demo(1,2,3,4,5,6,name="Aijan",age=23))


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

# Условие

# Напишите функцию show_data, которая:

# принимает любое количество позиционных аргументов
# принимает любое количество именованных аргументов
# выводит:
#  • сначала все позиционные аргументы
#  • затем все именованные аргументы в формате ключ = значение
# Пример вызова show_data(10, 20, 30, name="Aijan", city="Bishkek")

def show_data(*tuples, **dicts):
    print(tuples)
    print(dicts)

show_data(1,2,'w',["py", 12],name='Abc', age=23)
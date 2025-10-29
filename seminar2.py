# #task_1

# a=int(input("Сан кириниз:"))
# if a>5:
#     b=True 
# else:
#     b=False 
# print(b)

# #task_2

# i1=int(input("Сан кириниз"))
# res=i1%2

# if res==0:
#     print(res==0)
# else:
#     print(res==0)

#task_3

# a=int(input("a нын мааниси:"))
# b=int(input("b нын мааниси:"))

# if a==b*2:

#     print("True")
# else:
#     print("False")

# #task_4

# i2=int(input("Бир сан кириниз:"))

# if i2%3==0:
#     print("Yes")
# else:
#     print("No")

# #task_5

# i3=int(input("Бир сан кириниз"))

# if i3%2==0:
#     print(i3)
# else:
#     i3+=1
#     print(i3)

# #task_6

# x=int(input("Бир саан кириниз:"))

# if x>3 and x<=8:
#     print("Yes")
# else:
#     print("No")

#task_7

# x1=int(input("Бир сан кириниз"))

# if x1>=5 and x1<15 and x1!=10:
#     print("Yes")
# else:
#     print("No")

# #task_8

# x2=int(input("Бир сан кириниз"))

# if x2<=5 or x2>10:
#     print("Yes")
# else:
#     print("No")

# #task_9

# x3=int(input("Бир сан кириниз"))

# if (x3>2 and x3<=6) or x3>10:
#     print("Yes")
# else:
#     print("No")

#task_10 

# x4=int(input("Бир сан кириниз"))

# if (x4<4 or x4>10) and (x4<=2 or x4>=6):
#     print("Yes")
# else:
#     print("No")

##task_11

# x5=int(input("Бир сан кириниз"))

# if x5<=3 or x5>5:
#     print("Yes")
# else:
#     print("No")

#task_12

# if x5>-3 and x5<=6:
#     print("Yes")
# else:
#     print("No")

# if x5>=4:
#     print("Yes")
# else:
#     print("No")

# if (x5>-2 and x5<=3) or x5>5:
#     print("Yes")
# else:
#     print("No")

# #task_13

# u=int(input("Атмосферага кируу бурчу:"))

# if u>=40 and u<=45:
#     print("Параметрыы оптимальны!")
# elif u<40 and u>0:
#     print("Корабль разрушится в атмосфере!")
# elif u>45 and u>0 and u<36034:
#     print("Контролируемый спуск невозможен!")
# else:
#     print("Ошибка!")

#task_14

x=int(input("x тын мааниси:"))
y=int(input("y тин мааниси:"))
y_line=0.5*x+4

if y>y_line:
    print("Higher")
elif y<y_line:
    print("Below")
else: 
    print("One line")
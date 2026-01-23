import math as m
# #task_2
# x=24
# y=31.4
# print(type(x))
# print(type(y))

# #task_3

# a,b=12,32
# diff=abs(a-b)
# print(diff)

# #task_4

# krtfl=int(290)
# meshok=int(25)
# num1=krtfl//meshok
# num2=krtfl%meshok
# print(num1)
# print(num2)

# #task_5

# h_1=int(13)
# m_1=int(25)
# h_2=int(19)
# m_2=int(40)
# start=h_1*60+m_1
# end=h_2*60+m_2
# result=end-start
# h=result//60
# m=result%60
# print(h)
# print(m)

#task_6

# old_price=int(input('Write old price:'))
# new_price=int(input('Write new price:'))
# res=round((new_price-old_price)*100/old_price,1)
# print(res)


#task_7


# x=int(input("Enter x:"))
# y=m.pow(m.e,(1/(1+m.pow(m.cos(x),2))))
# print(y)

#task_8

# dt=1500
# person1=45
# result=m.ceil(dt/person1)
# print(result)


#task_9


# a=int(input("Введите длину катета:"))
# b=int(input("Введите длину катета:"))
# c=int(input("Введите длину гипотенузы:"))
# sin=min(a,b)/c
# print("Тар бурчтун синусу:",sin)

#task_10

katet_1=int(input("Введите длину катета:"))
katet_2=int(input("Введите длину катета:"))
gip=int(input("Введите длину гипотенузы:"))
sinus=min(katet_1,katet_2)/gip
burch1=m.degrees(m.asin(sinus))
burch2=sinus*180/m.pi
print(burch1)
print(burch2)
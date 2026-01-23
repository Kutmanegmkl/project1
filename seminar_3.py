# #task_1
# a=32
# b=3.5
# x=True
# a_str=str(a)
# b_str=str(b)
# x_str=str(x)

# #task_2
# str_="Hello my friend!"                                                                                                                                                                                                                                                                                                            

# #task_3, task_4
# name=input("Write your name:")
# surname=input("Write your surname:")
# res=name+","+surname
# print(res)

# #task_5
# name1=input("Enter your name")
# score=int(input("Score"))
# print(f"Hello,{name1}! Your score is {score}")

#task_7

str="Python is easy"
# print(str[0])
# print(str[-1])
# print(str[:2])
# print(str[-3:])
# print(str[2:5])
# print(str[1:8])
# print(str[1:-2])
# print(str[0::2])
# print(str[1::2])
# print(str[::-1])
# print(str[2:5])
# print(str[::-2])

# str1=["PythonProgrmmingLanguage"]
# line1=str1[0:6]
# line2=str1[-8:]

# #task_10

# name=input("Wath is your name?")
# name=name.capitalize()
# print(f"Hi,{name}")


# #task_15

# text = """ Имя этого героя "name". Поход в театр для него целый ритуал. Входя в фойе, "name" демонстративно снимает шляпу, поправляет галстук и вешает
# ольто на руку. Он непременно думает, что все, кому он знаком говорят про себя: "Ах, сегодня "name" неотразим!" После чего "name"
# занимает лучшее место бенуара и с важным видом достает очки."""
# name=input("Whats your name?")
# text1=text.replace("name",name)
# print(text1)

#task_16



str_ = '84hj#55hjl'
str1=str_.replace('#','#abc')
print(str1)

# #task_17

# tel = '0777784500'
# part1=tel[1:4]
# part2=tel[4:-3]
# part3=tel[-3:]
# tel1='+996 ('+part1+") "+part2+"-"+part3
# print(tel1)

# #task_18
# stroka=input("Enter string")
# if len(stroka)>5:
#     stroka=input("Write something:")
# if len(stroka)<=5:
#     print(stroka)
    
#task_20
password=input("Pasword:")
if password.find('#')==-1 and password.find('@')==-1 and password.find('%')==-1:
    password=input('Invalid password. Please re-enter!')
    if password.find('#')==-1 or password.find('@')==-1 or password.find('%')==-1:
        print("You have exhausted the number of attempts!")
    else:
        print(f"Password:{password} saved!")
else:
    print(f'Password {password} saved!')

#task_21

# name_list = 'айданургулсайкалаймээржылдызбакытайчолпонмадинажаныбекбекжолдостукэлиябатыржанаталмазбекчингизталанталтынбекмаратсаматтайырбеказаматбекмуратасанбек'
# name=input('Enter your name:')
# name1=name.lower()
# if name1 in name_list:
#     print("Поздравляю, вам положена повышенная стипендия.")
# else:
#     print("Увы, Вашего имени в списке нет")

    



    




     





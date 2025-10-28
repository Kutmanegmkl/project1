# person=input("ststus of the person")

# if person== 'student' or person=='school 10th' or person=='school 11th':
#     print(f'Сиз {person} болгонунуз учун кабыл алындыныз')

# else:
#     print(f"Сиз {person} болгнунузга байланыштуу сизди кабыл ала албайбы")


person=(input("How old are you?"))

if type(person)!=int:
     print("Сан кириниз!")
else:
    if person>0:
        if person<=6:
            print("Мектепке чейинкилер учун каана")
        elif person<18 and person>=7:
            print("Оспурумдор учун каана")
        elif person>=18 and person<=45:
            print('Орто жаштар учун каана')
        elif person>45 and person<=65:
            print('Улгайгандар учун каана')
        else:
            print("Улгайгандар учун каана")

    else:
            print("Жашынызды туура эмес жаздыныз!")          

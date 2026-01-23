#task_15
import math 
x=10
y=15
r=5
ad=eo=x
ae=do=y
oc=r
of=1.1*r
ao=(ad**2+do**2)**0.5
oac=math.degrees(math.asin(oc/ao))
ac=oc/math.tan(oac)
oad=math.degrees(math.asin(do/ao))-oac
oaf=math.degrees(math.asin(of/ao))
jad=oad-oac
had=oad-oaf
jah=oad-(oac+had)
b=had
e=jah
a=oac*2

f=float(input("Gradustuk chendi kirgiziniz:"))

if f>=0 and f<=90:
    if f<=b:
        print("Оптимальный курс!")
    elif f>b and f<=(b+e):
        print("Возмите правее!")
    elif f>(b+e) and f<=(b+e+a):
        print("Вы попадете в грозу!")
    elif f>(b+e+a) and f<=(b+e*2+a):
        print("Возмите левее!")
    elif f>(b+e*2+a) and f<=90:
        print("Оптимальный курс!")
else:
    print("Градустук чен туура эмес берилди!")







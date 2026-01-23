# Задание 1. ООП

class Animal:
    def __init__(self,name):
        self._name=name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof"
    

a=Animal("Unknown")
b=Dog("Rex")

print(a.speak())
print(b.speak())


# Задание 2. Функции

def count_words(text:str)->int:
    words=text.split()
    return len(words)

print(count_words("efio erveovied evecdsdc sdvd dd ddd d"))


# Задание 3. Объудиненное условие 


class TextAnalyzer:
    def __init__(self,text):
        self.text=text

    def analyze(self):
        return count_words(self.text)
    
analyzer=TextAnalyzer("I am Kuti")
print(analyzer.analyze())
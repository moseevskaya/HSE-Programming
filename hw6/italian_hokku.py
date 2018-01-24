import random

def read ():
    f = open('words_for_hokku.txt', 'r')
    lines = f.readlines()
    return lines

def array (num):
    a = read()[num].split()
    return a

#слова
def art ():
    return random.choice(array(0))

def noun2 ():
    return random.choice(array(1))

def noun3 ():
    return random.choice(array(2))

def noun4 ():
    return random.choice (array(3))

def verb2_2 ():
    return random.choice(array(4))

def verb2_1 ():
    return random.choice(array(5))

def adj2 ():
    return random.choice(array(6))
    
def adj3 ():
    return random.choice(array(7))

def punctuation():
    marks = [".", "?", "!", "...", " "]
    return random.choice(marks)

#строки
def hokku_5_1 ():
    return verb2_1() + ' ' + art() + ' ' + noun2() + punctuation()

def hokku_5_2 ():
    return art() + ' ' + noun2() + ' ' + verb2_2() + punctuation()

def hokku_7_1 ():
    return art() + ' ' + noun3() + ' ' + adj3() + punctuation()

def hokku_7_2 ():
    return art() + ' ' + noun4() + ' ' + adj2() + punctuation()

#создание
def create_hokku_5 ():
    hokku = random.choice([1,2])
    if hokku == 1:
        return hokku_5_1()
    else:
        return hokku_5_2()

def create_hokku_7 ():
    hokku = random.choice([1,2,3, 4, 5, 6, 7, 8, 9])
    if hokku == 1:
        return hokku_7_1()
    else:
        return hokku_7_2()


#вывод результата
print(create_hokku_5())
print(create_hokku_7())
print(create_hokku_5())

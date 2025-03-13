import random
abc="абвгдежзиклмнопрстуфхцчшщъыьэюя"

def atbash(text): #шифрование == дешифрование 
    text = str(text).lower()
    a = ""
    for i in text:
        a += abc[-1 - abc.find(i)]
    return a

def caesar(text, k): #шифр цезаря 
    itog = ""
    for j in text:
        a = abc.find(j)
        if a + k > 30:
            itog += abc[abs(31 - (a + k))]
        else:
            itog += abc[a + k]
    return itog

def caesar_dec(text, k): #шифр цезаря 
    itog = ""
    for j in text:
        a = abc.find(j)
        if a - k < 0:
            itog += abc[31 + (a - k)]
        else:
            itog += abc[a - k]
    return itog

abc = " абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,"
abc = ''.join(random.sample(abc,len(abc)))
square = [
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
]
for i in range(6): #случайно заполняем  матрицу
    for j in range(6):
        square[i][j] = abc[0]
        abc = abc[1:]

def polybian(text): # Полибианский квадрат
    for i in square: #вывод квадрата
        print(i)  
    itog = ""
    for i in text: #шифровка
        for o in range(6):
            for n in range(6):
                if i == square[o][n] and o != 5: #не прижат!
                    itog += square[o + 1][n]
                elif i == square[o][n] and o == 5: #прижат к полу
                    itog += square[0][n]
    return itog   
    
def polybian_dec(de_text):
    itog = ""
    for i in de_text: #дешифровка
        for o in range(6):
            for n in range(6):
                if i == square[o][n] and o != 0: #не прижат!
                    itog += square[o - 1][n]
                elif i == square[o][n] and o == 0: #прижат к потолку
                    itog += square[5][n]
    return itog                

abc="абвгдежзиклмнопрстуфхцчшщъыьэюя"
def numbers(key, num): # шифровка цифр
    itog = ""
    for i in num:
        if i in "1234567890":
            itog += key[int(i)]
        else:
            itog += i
    return itog

def numbers_dec(key, de_text):
    itog = ""
    for i in de_text:
        if i in key:
            itog += str(key.index(i))
        else:
            itog += i
    return itog
        

def gronsfeld(num, text): # шифр Гронсфельда
    itog = ""
    number = ""
    a = 0
    abc1 = abc.upper()
    text = text.upper()
    for i in text: #циклически расставляем числа
        if i in abc1:
            number += num[a]
            a += 1
            if len(num) == a:
                a = 0
        else:
            number += " "
    for i in range(len(text)): #шифровка
        if text[i] == " ":
            itog += " "
        elif abc1.find(text[i]) + int(number[i]) >= 31:
            itog += abc1[abs(31 - (abc1.find(text[i]) + int(number[i])))]
        else:
            itog += abc1[abc1.find(text[i]) + int(number[i])]
    return itog

def gronsfeld_dec(num, de_text):
    itog = ""
    number = ""
    a = 0
    abc1 = abc.upper()
    de_text = de_text.upper()
    for i in de_text: #циклически расставляем числа
        if i in abc1:
            number += num[a]
            a += 1
            if len(num) == a:
                a = 0
        else:
            number += " "
        itog = ""
    for i in range(len(de_text)): #дешифровка
        if de_text[i] == " ":
            itog += " "
        elif abc1.find(de_text[i]) - int(number[i]) < 0:
            itog += abc1[abs(31 + (abc1.find(de_text[i]) - int(number[i])))]
        else:
            itog += abc1[abc1.find(de_text[i]) - int(number[i])]
    return itog

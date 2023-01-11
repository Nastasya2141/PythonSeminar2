
def Task1():
#Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
#пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
    number = int (input('Введите число N: ')) 
    result =[]
    factorial = 1
    for i in range(1,number+1):
        factorial*=i
        result.append(factorial)
    print(f'Список факториалов от 1 до {number} -> {result}')


def Task2():
#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
    print(' x | y | z | not(X and Y) or Z.')
    for x in range (2):
        for y in range(2):
            for z in range(2):
             print(f' {x} | {y} | {z} | {int(not (x and y) or z)}')



def Task3():
#Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
#«one» «onetwonine» - o – 2, n – 3, e – 2
    phrase = 'one'
    text = 'onetwonine'
    for i in range(len (phrase)):
        count = 0
        phrase_part = phrase[i]
        for x in range(len (text)):
            text_part = text[x]
            if phrase_part == text_part:
                count += 1
        print (f'{phrase_part} - {count}')


def Task4():
#Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
#3 -> [2, 3, -3, -2, -1, 0, 1]
    number = int (input('Введите число N: ')) 
    result = []
    for i in range(-number,number+1):
        result.append(i)
    print (result)
    result = result[-2:] + result[:-2]
    print (result)

   



   





#Task1()
#Task2()
#Task3()
#Task4()
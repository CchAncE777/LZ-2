
#рекурсивные функции
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

#вычисление суммы натуральных чисел от 1 до n
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print(sum(5))

#Проверка строки на палидромность
def IsPalindrome(S):
    if len(S) <= 1:
        return True
    else:
        return S[0] == S[-1] and IsPalindrome(S[1:-1])

IsPalindrome('12321')

#Суммирование строки
def Sum(A):
    if len(A) == 0:
        return 0
    else:
        return Sum(A[:-1]) + A[-1]

list_A = [1, 2, 3, 4, 5, 6, 7]
Sum(list_A)

#Наибольшее значение в списке
def Max(A):
    if len(A) == 1:
        return A[0]
    else:
        return max(Max(A[:-1]), A[-1])

list_A = [1, 2, 3, 4, 5, 6, 7]
Max(list_A)

#Числа фибонначи
def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)
    
Fib(11)

#Быстрое возведение в степень
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        return power(a, n // 2) ** 2
    

power (2, 10)

#Ханойские башни
def move(n, start, finish):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n - 1, temp, finish)
# Для решения головоломки из 10 дисков вызываем так:
move(10, 1, 3)

def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        move(n - 1, temp, finish)
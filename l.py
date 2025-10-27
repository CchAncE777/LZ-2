l_b = input('Введите ряд чисел: ')
list =  [int(num) for num in l_b.split()]
jump = int(len(list)**(1/2))
iskomoe = int(input('Введите число из списка: '))
index = 0
is_found = False

for i  in range(0, len(list), jump):
    if iskomoe <list[i]:
        for j in range(i-len(list), i):
            if list[j] == iskomoe:
                index = j
                is_found = True
                break
    if list[index] == iskomoe:
         break
for j in range(i, len(list)):
            if list[j] == iskomoe:
                index = j
                is_found = True
                break

if is_found:
    print(index)
else:
     print('Not found. Число не найдено')
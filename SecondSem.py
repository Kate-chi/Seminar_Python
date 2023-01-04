# По данному целому неотрицательному n вычислите значение n!.
#  N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# Input: 5
# Output: 120

# num = int(input('Введите число: '))
# res = 1

# if num == 0:
#     print(1)
#     exit()

# while num > 1:
#     res *= num
#     num -= 1
    
# print(res)

# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.\

# def fibonache(n):
#     if n == 1:
#         return 2, 3
#     number0 = 0
#     number1 = 1
#     count = 2
#     while n >= number1:
#         if n == number1:
#             return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1

# num2 = int(input('Введите число: '))
# print(fibonache(num2))

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random
n = 35
m = []
count = 0
max = 0
for i in range(0, n):
    random_num = round(random.randint(-50, 50))
    m.append(random_num)
    if m[i] < 0 : count = 0
    if m[i] > 0 :
        count +=1
    if max < count : max = count

print(m)

print(max)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

def arbuzLine(N):
    arbuzes=[]
    for _ in range(N):
        arbuzes.append(random.randint(5000,30000))
    arbuzes.sort()
    print(arbuzes)

# min=max=arbuzes[0]
# for item in arbuzes:
# if min>item: min = item
# elif max < item: max = item

# return min, max

    return arbuzes[0],arbuzes[-1]


num3 = int(input('Введите число: '))
print(arbuzLine(num3))
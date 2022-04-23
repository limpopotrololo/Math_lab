import math
import random

import matplotlib.pyplot as plt

# границы интегрирования
a = 0
b = math.pi


# исходная функция
def f(x):
    return math.sin(2 * x)  # функция, данная по заданию


# ниже 4 функции для получения интегральных сумм для различных методов оснащений
# для левого и правого способа оснащения различия функций в начале и конце итерируемого списка
# для центрального и случайного оснащения пользуемся половинным шагом и функцие random в промежутке конкретного шага соответсвенно
# для отрисовки процесса есть функция risovashka ей передается кринж лист значений и по нему она рисует гистрограмму и график

def left_integral():
    ans = []
    pop = []
    intsum = 0
    for i in range(0, n):
        global a, step
        intsum += f(a + i * step)

        pop.append(f(a + i * step))
    ans.append(intsum)
    ans.append(pop)
    return ans


def right_integral():
    intsum = 0
    pop = []
    ans = []
    global a
    for i in range(1, n + 1):
        intsum += f(a + i * step)
        pop.append(f(a + i * step))
    ans.append(intsum)
    ans.append(pop)
    return ans


def central_integral():
    pop = []
    ans = []
    intsum = 0
    global a, step
    h = step / 2
    x = a
    for i in range(1, n + 1):
        intsum += f(x + h)
        pop.append(f(x + h))
        x = i * step
    ans.append(intsum)
    ans.append(pop)
    return ans


def random_integral():
    pop = []
    ans = []
    intsum = 0
    global a
    for i in range(1, n + 1):
        intsum += f(random.uniform(a, i * step))
        pop.append(f(random.uniform(a, i * step)))
        a = i * step
    ans.append(intsum)
    ans.append(pop)
    return ans


def risovashka(cringe):
    x = a
    bin = []
    for i in range(1, n + 1):
        bin.append(x)
        x = i * step
    colors = ['blue', 'red']
    plt.figure(figsize=(10, 10))
    plt.bar(bin, cringe, color=colors, width=3.15 / n)
    plt.plot(bin, cringe)
    plt.show()


n = int(input("Введите количество точек разбиения \n"))
step = (b - a) / n
var = int(input("1-лево, 2-право, 3-центр, 4-как получится \n"))

if var == 1:
    print("left " + str(left_integral()[0] * step))
    risovashka(left_integral()[1])
elif var == 2:
    print("right " + str(right_integral()[0] * step))
    risovashka(right_integral()[1])
elif var == 3:
    print("central " + str(central_integral()[0] * step))
    risovashka(central_integral()[1])
elif var == 4:
    print("random " + str(random_integral()[0] * step))
    risovashka(random_integral()[1])
else:
    print("Попробуйте еще")

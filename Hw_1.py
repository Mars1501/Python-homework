# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day_number = int(input("Введите номер дня недели: "))

# if 0 < day_number < 8:
#     if day_number > 5:
#         print("day off")
#     else:
#         print("not a day off")
# else:
#     print("Введите кореектный номер дня недели")


# Напишите программу для. проверки истинности утверждения ¬(x ⋁ y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (x и y), причём x ≠ 0 и y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))

# if x > 0 and y > 0:
#     print("Первая четверть")
# elif x < 0 and y > 0:
#     print("Вторая чтеверть")
# elif x < 0 and y < 0:
#     print("Третья четверть") 
# elif x > 0 and y < 0:
#      print("Чертвертая четверть")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math
# from turtle import distance
# x1 = int(input("Введите коордтнату х1: "))
# y1 = int(input("Введите коордтнату y1: "))
# x2 = int(input("Введите коордтнату х2: "))
# y2 = int(input("Введите коордтнату y2: "))
# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(round(distance, 2))
# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?

# Входные данные
# Программа получает на вход числа N и K.

# Выходные данные
# Программа должна вывести искомое количество яблок.

n = int(input())
k = int(input())

apples_per_student = k // n

print(apples_per_student)
# Вывести на экран числа от -N до N

# n=int(input('Введите  число n > 0 и жми пуск '))
# print('Ваше число = ',n)
# for i in range(-n,n+1):
#     if i!=0:    # Если N - это множество натуральных чисел, то, в России, число ноль не принадлежит множеству (N) натуральных чисел.
#      print(i)

n=int(input('Введите  число n > 0 и жми пуск '))
print('Ваше число = ',n)
ran=range(-n,n+1)
f=list(ran)
print(f)

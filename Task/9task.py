# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

n=int (input('Введите номер квадранта плоскости координат = '))

v='Допустимые значения координат:'
a='x>0; y>0;'
b='x<0; y>0;'
c='x<0; y<0;'
d='x>0; y<0;'
if n==1:
    print(v,a)
elif n==2:
    print(v,b)
elif n==3:
    print(v,c)
elif n==4:
    print(v,d)
else:
    print(' -ХВАТИТ БАЛОВАТЬСЯ!')
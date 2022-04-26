# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

fx=[0,1]
fy=[0,1]
fz=[0,1]
flag=1
for i in fx:
    for j in fy:
        for k in fz:
            f1 = not(fx[i] or fy[j] or fz[k]) 
            f2 = ((not fx[i]) and (not fy[j]) and (not fz[k]))
            print(f1,'   ',f2,'   ',i,j,k)
            if  f1!=f2:
                flag=0
if flag == 1:
    print('утверждение верно')
else:
    print('утверждение ложно')
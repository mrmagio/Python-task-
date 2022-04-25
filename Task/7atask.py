# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

flag=1
for i in 0,1:
    for j in 0,1:
        for k in 0,1:
            print(i,j,k)   
            f1 = (not (i or j or k)==((not i) and (not j) and ( not k)))
            if f1 !=1:
                flag=0                 
                print(f1)            
if flag==0:
    print('Утверждение ложно')
else:
    print('утверждение истинно')

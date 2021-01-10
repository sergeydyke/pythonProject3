from random import randint
num=[]
for i in range(15):
     num.append(randint(0,9))
print('Рандомний список', num)
n = int(input('Введіть число, яке потрібно знайти',))
if num.count(n)==0:
    print('Таке число відсутнє!')
else:
    print('Твоє число під номером:', num.index(n)+1)



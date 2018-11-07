# -*- coding: cp1251 -*-
import random
n=random.randrange(2,5)
answer=input('Выберите одну из трех дверей?:')
if answer==3:
    print('Вы не угадали')
    if answer<=3:
        print('Вам повезет в следующий раз')
        answer=input('Не желаете ли Вы изменить свой выбор?')
        if answer=='нет':
            print('Хорошо, это Ваше право')
       else:
           return(n)

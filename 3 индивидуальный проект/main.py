from pip._vendor.distlib.compat import raw_input

from servstart import * 
from telegrambot import *




if __name__ == '__main__':
    print('Введите нужную цифру:\n'
          '1 - Проверка сервера\n'
          '2 - Бот\n'
          '3 - загрузить в sql\n'
          'или "q" для выхода')
    inp=['']

    while inp!='q':
        inp=raw_input()
        if inp!='q':
            if inp=='1':
                telbot = TelBot()                
            else:
                print("Введено неправильное число")
            print('Введите нужную цифру:\n'
          '1 - Проверка сервера\n'
          '2 - Бот\n'
          '3 - загрузить в sql\n'
          'или "q" для выхода')
    else:
        try:
            telbot.t.do_run = False
            telbot._updater.stop()
        except NameError:
            print('Выход') 
        print('end')                
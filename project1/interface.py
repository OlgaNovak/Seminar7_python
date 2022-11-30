import info,digit,log

def button_click():
    print('Введите "0", если хотите продолжить')
    print('Введите "1", если хотите закончить')
    flag=int(input())
    while flag==0:
        v=digit.parse()
        info.view_data(v)
        log.loger1(v)
        log.loger2(v)
        print('Введите "0", если хотите продолжить')
        print('Введите "1", если хотите закончить')
        flag=int(input())
    print("Программа завершилась")



password = True
while password:
    if input('введите ваш пароль: ') == "geg":
        print('добро пожаловать!!!', end = ' ')
        password = False
    else:
        print("ваш пароль неверный, попробуйте еще раз...", end= "")



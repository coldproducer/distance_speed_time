print("Введите значения известных переменных, если переменная не известна, то введите 0")
s = float(input("Введите значение переменной s: "))
v = float(input("Введите значение переменной v: "))
t = float(input("Введите значение переменной t: "))

if s == 0 and v != 0 and t != 0:
    print("Найдём расстояние(s) путём умножения скорости(v) на время(t)")
    s = v*t
    print("Расстояние равно: ",s)
elif v == 0 and s != 0 and t != 0:
    print("Найдём скорость(v) путём деления расстояния(s) на время(t)")
    v = s/t
    print("Скорость равна: ",v)
elif t == 0 and s != 0 and v != 0:
    print("Найдём время(t) путём деления расстояния(s) на скорость(v)")
    t = s/v
    print("Время равно: ",t)
elif (s == 0 and v == 0) or (s == 0 and t == 0) or (v == 0 and t == 0) or (s == 0 and v == 0 and t == 0):
    print("Неизвестны две или более переменных")
else:
    if s/v == t:
        print("Все переменные известны и корректны:)")
    else:
        print("Вы указали неверные значения переменных")
    
    

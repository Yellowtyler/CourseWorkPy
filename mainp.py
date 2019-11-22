from math import*
from datetime import datetime
#функция
def funct(f,x):
    new_f = f.replace('x', str(x))
    y = eval(new_f)
    return y
#производная
def dif(x,f,difx = 0.000000001):
    lf = funct(f,x + difx)
    rf = funct(f,x)
    return (lf - rf) / difx
#метод итераций
def iter(x,e,f):
    start = datetime.now()
    i=0
    l = 1/dif(x,f)
    while True:
     try:
        f1= funct(f, x)
        x = x - l*f1
        i+=1

        if abs(f1)<=e:
            break
     except ValueError:
         x = abs(x)
    print(datetime.now()-start)
    print("Было сделано " + str(i)+ " итераций.")
    print("Корень уравнения равен: ")
    return x
#метод Ньютона
def newton(x,e,f):
 start = datetime.now()
 i=0
 while True:
     try:
         df = dif(x,f)
         f1 = funct(f,x)
         x = x - f1/df
         i+=1
         if abs(f1)<=e:
             break
     except ValueError:
         x=abs(x)
     except ZeroDivisionError:
         x=2
         break
 print(datetime.now() - start)
 print("Было сделано " + str(i) + " итераций.")
 print("Корень уравнения равен: ")
 return x
#метод Дихотомии
def dih(x0,x1,e,f):
    start = datetime.now()
    i=0
    l=x0
    r=x1
    while True:
     try:
        x = (l+r)/2
        f1 = funct(f,x)
        f2 = funct(f,r)
        if(f1 < 0 and f2 < 0) or (f1 > 0 and f2> 0):
            r = x
        else:
            l = x
        i+=1
        if abs(r-l)<=e:
         break
     except ValueError:
         x = abs(x)
    print(datetime.now() - start)
    print("Было сделано " + str(i) + " итераций.")
    print("Корень уравнения равен: ")
    return x
#вывод результатов
def out(a):
    print("Вы выбрали ", a[1])
    print ("Точность, которую вы выбрали: ",a[2])
    print("Корень уравнения: ", a[0])
#запись в файл
def wr(a):
    while True:
        try:
            st = input("Введите имя файла:")
        except FileNotFoundError:
            print("Ошибка. Файл не найден. Введите названия файла еще раз:")
        else:
            break
    fil = open(st, 'w')
    for i in range(len(a)):
        fil.write(str(a[i]) + "\n")
    fil.close()
#результаты последнего сеанса
def lastse():
    while True:
        try:
            st = input("Введите имя файла:")
        except FileNotFoundError:
            print("Ошибка. Файл не найден. Введите названия файла еще раз:")
        else:
            break
    print("////Ваш прошлый сеанс////")
    fil1 = open(st, 'r')
    print("f(x) = " + fil1.readline())
    print("x = " + fil1.readline())
    print("Результат был получен Методом " + fil1.readline())
    print("Точность: " + fil1.readline())
    print("///////////////")
    fil1.close()
#консольное меню
def main():
 choice=4
 f = input("Введите функцию (Аргументом обязательно должен быть x!):")
 toch=0.00001
 x0=5
 x1=0
 print(iter(x0,toch,f))
 print(newton(x0,toch,f))
 print(dih(x1,x0, toch, f))
 while choice!=0:

   while True:
    try:
     f = input("Введите функцию (Аргументом обязательно должен быть x!):")
     if "x" not in f:
         print("Не найден x! Аргументом обязательно должен быть x!")
         continue
     x0 = int(input("Введите число:"))
     if x0<=0:
         print("Введите положительно число!")
         continue
     eps= float(input("Введите точность:"))
     if abs(eps)>1:
         print("По условию модуль точности должен быть меньше 1!")
         continue
    except  ValueError:
      print("Ошибка. Введите число.")
    else:
      break
   #new_f = f.replace('x',str(x0))
   #y= eval(new_f)
   #print(y)
   print("1. Метод итераций\n2. Метод Ньютона\n3. Метод дихотомии\n0. Выход\nВыберите операцию, которую хотите совершить:")
   while True:
    try:
     choice = int(input())
     if 0<=choice<=3:
       break
    except  ValueError:
      print("Ошибка. Введите число.")
    else:
      break
   a=[]
   a.append(f)
   if choice == 1:
     a.append(iter(x0,eps,f))
     a.append("итераций")
   elif choice == 2:
     a.append(newton(x0, eps,f))
     a.append("Ньютона")
   elif choice == 3:
     x1=0
     a.append(dih(x1,x0,eps,f))
     a.append("дихотомии")
   elif choice == 0:
      break
   a.append(eps)
   print(a[1])
   print("1. Вывод результатов текущего сеанса\n2. Записать в файл\n3. Вывод результатов прошлого сеанса из файла\n0. Выход\nВыберите операцию, которую хотите совершить:")
   while True:
     try:
         choice = int(input())
         if 0 <= choice <= 3:
             break
     except  ValueError:
         print("Ошибка. Введите число.")
     else:
         break
   if choice == 1:
     print("///////////////")
     out(a)
     print("///////////////")
   elif choice == 2:
     print("///////////////")

     wr(a)
     print("///////////////")
   elif choice == 3:
      lastse()
   elif choice == 0:
     break
   if choice !=2:
       print("Хотите записать данные в файл?(Да(1)/Нет(0))")
       while True:
         try:
             choice = int(input())
             if 0 <= choice <= 1:
                 break
         except  ValueError:
             print("Ошибка. Введите число.")
         else:
             break
       if choice == 1:
           wr(a)
       else:
           break
main()
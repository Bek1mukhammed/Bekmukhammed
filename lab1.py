#zadanie1
print(4,8,15,46,23,42, sep=' ')
#zadanie2

print(4,8,15,46,23,42, sep='\n')
#zadanie3

a = int(input())
for i in range(1,3):
     print(a+i)
  #zadanie4
try:

    num1 = int(input("первое число: "))
    num2 = int(input("второе число: "))
    num3 = int(input("третье число: "))


    total = num1 + num2 + num3


    print(total)
except ValueError:
    print("Ошибка: целое число.")
  #zadanie6
try:

    mandarins = int(input("мандарины: "))
    students = int(input("школьникы: "))

    per_student = mandarins // students


    remaining = mandarins % students


    print(f"Каждый школьник получит {per_student} целых мандаринов.")
    print(f"Останется {remaining} целых мандаринов в корзине.")
except ValueError:
    print("Ошибка: Введите целые числа (количество мандаринов и школьников).")
  #zadanie7
try:

    number = input("четырёхзначное число: ")

    # Проверка, что введенное значение имеет четыре цифры
    if len(number) != 4:
        print("Ошибка: Введите четырёхзначное число.")
    else:

        thousands = int(number[0])
        hundreds = int(number[1])
        tens = int(number[2])
        units = int(number[3])


        print(f"The digit in the thousands position is {thousands}")
        print(f"The digit in the hundreds position is {hundreds}")
        print(f"The digit in the tens position is {tens}")
        print(f"The digit in the position of units is {units}")
except ValueError:
    print("Ошибка: Введите четырёхзначное число.")
  #zadanie7
try:

    number = input("четырёхзначное число: ")

    # Проверка, что введенное значение имеет четыре цифры
    if len(number) != 4:
        print("Ошибка: Введите четырёхзначное число.")
    else:

        thousands = int(number[0])
        hundreds = int(number[1])
        tens = int(number[2])
        units = int(number[3])


        print(f"The digit in the thousands position is {thousands}")
        print(f"The digit in the hundreds position is {hundreds}")
        print(f"The digit in the tens position is {tens}")
        print(f"The digit in the position of units is {units}")
except ValueError:
    print("Ошибка: Введите четырёхзначное число.")
  #zadanie9
try:
    # Ввод числа от пользователя
    num = int(input("Введите целое число: "))

    # Выполнение побитового сдвига влево на один бит
    result = num << 1

    # Проверка результата и вывод сообщения
    if result == 0:
        print("Предупреждение: Результат равен нулю.")
    else:
        print(f"Результат операции << равен {result}")
except ValueError:
    print("Ошибка: Введите целое число.")
  #zadanie10
try:

    num1 = float(input("Пожалуйста, введите первое число: "))
    num2 = float(input("Пожалуйста, введите второе число: "))


    operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: Деление на ноль недопустимо.")
        else:
            result = num1 / num2
    else:
        print("Ошибка: Неверная операция.")

    if operation in ('+', '-', '*', '/'):
        print(f"{num1} {operation} {num2} = {result}")
except ValueError:
    print("Ошибка: Введите числа в правильном формате.")

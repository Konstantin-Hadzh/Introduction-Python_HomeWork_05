

''' 5) Создать (программно) текстовый файл, записать в него программно 
    набор чисел, разделенных пробелами. Программа должна подсчитывать сумму 
    чисел в файле и выводить ее на экран '''
    
    
def summary():
    try:
        with open('set_numbers.txt', 'w', encoding = 'utf-8') as iter_f:
            line = input('Введите цифры через пробел: ')
            iter_f.writelines(line)
            num_input = line.split()

            print(sum(map(int, num_input)))
    except ValueError:
        print('Ошибка')
summary()
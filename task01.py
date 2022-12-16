

''' 1) Создать программно файл в текстовом формате, записать в него построчно 
    данные, вводимые пользователем. Об окончании ввода данных свидетельствует 
    пустая строка '''
    
homework_file = open('proba.txt', 'w')
text_form = input('Введите данные: ')
while text_form:
    homework_file.writelines(text_form)
    text_form = input('Введите данные: ')
    if not text_form:
        break

homework_file.close()
homework_file = open('proba.txt', 'r')

homework_file.close()
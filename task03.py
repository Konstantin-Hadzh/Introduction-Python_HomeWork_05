

''' 3) Создать текстовый файл (не программно), построчно записать фамилии 
    сотрудников и величину их окладов (не менее 10 строк). Определить, 
    кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих 
    сотрудников. Выполнить подсчет средней величины дохода сотрудников.
    Пример файла:
    Иванов 23543.12
    Петров 13749.32 '''

with open('bet.txt', 'r') as bet_file:
    min_bet = []
    average_bet = []
    bet_list = bet_file.read().split('\n')
    for i in bet_list:
        i = i.split()
        if float(i[1]) < 20000:
            min_bet.append(i[0])
        average_bet.append(i[1])
        
print(f'Оклад меньше 20000 {min_bet}, \nсредний оклад {sum(map(float, average_bet)) / len(average_bet)}')
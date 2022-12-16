

''' 4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на 
русские. Новый блок строк должен записываться в новый текстовый файл '''

block_rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_block = []
with open('eng_num.txt', 'r') as iter_1:
    for i in iter_1:
        i = i.split(' ', 1)
        new_block.append(block_rus[i[0]] + ' ' + i[1])
    
with open('rus_num.txt', 'w') as iter_2:
    iter_2.writelines(new_block)
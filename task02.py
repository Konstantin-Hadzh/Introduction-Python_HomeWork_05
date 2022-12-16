

''' 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, 
    выполнить подсчет количества строк, количества слов в каждой строке '''
    

def count_lines_words():
    try:
        with open('not_program_file_1.txt', 'r', encoding = "utf-8") as file:
            list_1 = file.readlines()
            for i in range(len(list_1)):
                list_2 = list_1[i].split()
                print(f'В сторке № {i + 1} -> {len(list_2)} слова')
    except FileNotFoundError:
        return 'Файл не найден'

count_lines_words()
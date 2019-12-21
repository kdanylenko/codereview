"""
Проверить наличие элемента в папке
Заданы:
Путь с элементами
Путь к элементу для проверки
"""

def file_search(folder, file_path):
    for path in file_path:
        for element in folder:
            if path == element:
                i = 1
                break
            else:
                i = 0
    if i:
        print("OK")
    else:
        print("Error")


first_folder = ['C:','r','backup.log','ideas.txt','hu5.txt']
needed_path = 'C:/r/ideas.txt'.split('/')


file_search(first_folder,needed_path)
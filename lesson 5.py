import os


def add_folder():
    try:
        os.mkdir(input('Введите имя новой папки:\n'))
        print('Успешно создано')
    except FileExistsError:
        print('Такая директория уже существует')


def del_folder():
    try:
        os.rmdir(input('Введите имя папки, которую хотите удалить\n'))
        print('Успешно удалено')
    except FileExistsError:
        print('Такая директория не существует')


def view_current_dir():
    print('Текущая директория:', os.getcwd())


def go_to_folder():
    add_path = input('Введите имя папки, в которую хотите перейти\n')
    if '.' in add_path:
        print('Файл не является папкой, переход не возможен')
    else:
        try:
            path = os.getcwd() + '\\' + add_path
            os.chdir(r'' + path)
            print('Успешно перешёл')
            return path
        except FileNotFoundError:
            print('Не возможно перейти в директорию')


def go_back():
    path = os.getcwd()
    if len(path) <= len(start_path):
        print('Перемещаться можно только в рамках проекта!')
    else:
        path = path[0:path.rindex('\\')]
        os.chdir(path)
        print('Успешно вернулся назад')
    return path


def view_files_in_dir():
    print(os.listdir(path))


start_path = path = os.getcwd()
i = ''
while i != 'exit':
    view_current_dir()
    i = input('1 - Перейти в папку\n2 - Вернуться назад\n3 - Просмотреть содержимое текущей папки\n4 - Создать папку\n'
              '5 - Удалить папку\nexit - Выход\n')
    if i == '1':
        path = go_to_folder()
    elif i == '2':
        go_back()
    elif i == '3':
        view_files_in_dir()
    elif i == '4':
        add_folder()
    elif i == '5':
        del_folder()
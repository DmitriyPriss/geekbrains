import sys
import random

file = open('log.txt', 'a')
figure = ['камень', 'ножницы', 'бумага']
list = [4, 1, 11, 5, 8, 15, 7, 13, 12, 16, 14, 2, 9, 6, 3, 10]
secret_list = ['|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|',
               '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|']
answer2 = ''
answer3 = ''
char = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
figure = ['камень', 'ножницы', 'бумага']


def game1():
    char_for_game = char
    print('Привет,', gamer['name'], '\nЯ могу назвать буквы алфавита, которых нет в твоем имени.')
    for i in gamer['name']:
        if i in char_for_game:
            char_for_game = char_for_game.replace(i, '')

    print('В твоём имени нет букв:')
    print(char_for_game)
    file.write("%-15s%-15s" % ('Игра:', '1') + '\n')
    file.write("%-15s%-15s" % ('Игрок:', gamer['name']) + '\n')
    file.write('В твоём имени нет букв:\n')
    file.write(char + '\n')
    file.write('\n')

def game2():
    list_for_game = list
    secret_list_for_game = secret_list
    print('Я задумал 16 чисел от 1 до 16 и расположил их в произвольном порядке в строке. Скажи мне где какое.')
    print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
    all_attempts = 0
    for i in range(len(list_for_game)):
        attempt = 0
        index = list_for_game.index(i + 1) + 1
        answer3 = input('Скажи мне, где число {}?\n'.format(i + 1))
        if answer3 == 'exit':
            return

        answer3 = int(answer3)
        while answer3 != index:
            attempt = attempt + 1
            answer3 = input('Не угадал! Попробуй ещё раз!\n')
            if answer3 == 'exit':
                return

            answer3 = int(answer3)
        print('Правильно! Ты угадал с', attempt + 1, 'раза!!!')
        all_attempts = all_attempts + (attempt + 1)
        secret_list_for_game[index * 2 - 1] = str(i + 1)
        print(''.join(secret_list_for_game))

    print('Ты победил!!!')
    file.write("%-15s%-15s" % ('Игра:', '2') + '\n')
    file.write("%-15s%-15s" % ('Игрок:', gamer['name']) + '\n')
    file.write('Все числа были угаданы с ' + str(all_attempts) + ' попытки.\n')
    file.write('\n')


def game3():
    ai = random.randint(0, 2)
    figure_gamer = input('Твоя фигура?\n')
    win = 0
    lose = 0

    while figure_gamer != 'exit':
        if figure[ai] == figure_gamer.lower():
            winner = 'Ничья'

        elif (figure[ai] == 'камень' and figure_gamer.lower() == 'ножницы') or \
                (figure[ai] == 'ножницы' and figure_gamer.lower() == 'бумага') or \
                (figure[ai] == 'бумага' and figure_gamer.lower() == 'камень'):
            win = win + 1
            winner = 'Компьютер'


        elif (figure[ai] == 'камень' and figure_gamer.lower() == 'бумага') or \
                (figure[ai] == 'ножницы' and figure_gamer.lower() == 'камень') or \
                (figure[ai] == 'бумага' and figure_gamer.lower() == 'ножницы'):
            lose = lose + 1
            winner = 'Игрок'

        info(figure[ai], figure_gamer, winner, win, lose)
        ai = random.randint(0, 2)
        figure_gamer = input('Твоя фигура?\n')

    file.write("%-15s%-15s" % ('Игра:', '3') + '\n')
    file.write("%-15s%-15s" % ('Игрок:', gamer['name']) + '\n')
    file.write('Cчёт:\n')
    file.write("%-15s%-15s" % ('Компьютер', 'Игрок') + '\n')
    file.write("%-15d%-15d" % (win, lose) + '\n')
    file.write('\n')


def info(figure_ai, figure_gamer, winner, win, lose):
    print("%-15s%-15s" % ('Компьютер', 'Игрок'))
    print("%-15s%-15s" % (figure_ai, figure_gamer.lower()))
    print("%-15s%-15s" % ('Победил:', winner))
    print('Cчёт:')
    print("%-15s%-15s" % ('Компьютер', 'Игрок'))
    print("%-15d%-15d" % (win, lose))


print('Своя игра')

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Какого ты пола?\n'),
         'pet_name': input('Как зовут твоего питомца?\n'),
         'love_games': input('Любишь ли ты играть?\n'),
         }

if gamer['age'] < 18:
    print('Тебе нет 18 лет, тебе нельзя играть')
    sys.exit()

elif gamer['age'] > 90:
    answer1 = input('Игра может быть сильно утомительной для вас.\nУверены ли, вы, что хотите играть?\n')

    if answer1.lower() == 'Да'.lower():
        answer2 = input('Точно?\n')

        if answer2.lower() == 'Да'.lower():
            print('Хорошо, тогда начнём игру!')

        elif answer2 == 'exit':
            sys.exit()

        else:
            print('До свидания,', gamer['name'])

    elif answer1 == 'exit':
        sys.exit()
    else:
        print('До свидания,', gamer['name'])

game = input('Выбери игру!\n1 - Букв которых нет в твоём имени.\n2 - Отгадай числа.\n3 - Камень, ножницы, бумага.\n'
             'exit - Выход из игры.\n')

while game != 'exit':
    if game == '1':
        game1()

    elif game == '2':
        game2()

    elif game == '3':
        game3()

    game = input('Выбери игру!\n1 - Букв которых нет в твоём имени.\n2 - Отгадай числа.\n3 - Камень, ножницы, бумага.\n'
                 'exit - Выход из игры.\n')

file.close()
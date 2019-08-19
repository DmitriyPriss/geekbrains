import sys

list = [4, 1, 11, 5, 8, 15, 7, 13, 12, 16, 14, 2, 9, 6, 3, 10]
secret_list = ['|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|',
               '*', '|', '*', '|', '*', '|', '*', '|', '*', '|', '*', '|']
answer2 = ''
answer3 = ''
char = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

print('Своя игра')

gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Какого ты пола?\n'),
         'pet_name': input('Как зовут твоего питомца?\n'),
         'love_games': input('Любишь ли ты играть?\n'),
         }

if gamer['age'] < 18:
    print('Тебе нет 18 лет, тебе нельзя играть')

elif gamer['age'] > 90:
    answer1 = input('Игра может быть сильно утомительной для вас.\nУверены ли, вы, что хотите играть?\n')
    if answer3 == 'exit':
        sys.exit()

    if answer1.lower() == 'Да'.lower():
        answer2 = input('Точно?\n')

        if answer2.lower() == 'Да'.lower():
            print('Хорошо, тогда начнём игру!')

        if answer2 == 'exit':
            sys.exit()

        else:
            print('До свидания,', gamer['name'])

    if answer1 == 'exit':
        sys.exit()
    else:
        print('До свидания,', gamer['name'])

if 18 <= gamer['age'] <= 90 or answer2.lower() == 'Да'.lower():
    print('Привет,', gamer['name'], '\nЯ могу назвать буквы алфавита, которых нет в твоем имени.')
    for i in gamer['name']:
        if i in char:
            char = char.replace(i, '')

print('В твоём имени нет букв:')
print(char)
print('Я задумал 16 чисел от 1 до 16 и расположил их в произвольном порядке в строке. Скажи мне где какое.')
print('|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|*|')
for i in range(len(list)):
    attempt = 0
    index = list.index(i + 1) + 1
    answer3 = input('Скажи мне, где число {}?\n'.format(i + 1))
    if answer3 == 'exit':
        sys.exit()

    answer3 = int(answer3)
    while answer3 != index:
        attempt = attempt + 1
        answer3 = input('Не угадал! Попробуй ещё раз!\n')
        if answer3 == 'exit':
            sys.exit()

        answer3 = int(answer3)
    print('Правильно! Ты угадал с', attempt+1, 'раза!!!')
    secret_list[index * 2 - 1] = str(i + 1)
    print(''.join(secret_list))

print('Ты победил!!!')
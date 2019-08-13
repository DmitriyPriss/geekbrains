print('Своя игра')
gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Какого ты пола?\n'),
         'pet_name': input('Как зовут твоего питомца?\n'),
         'love_games': input('Любишь ли ты играть?\n'),
         }

question2 = ''

if gamer['age'] < 18:
    print('Тебе нет 18 лет, тебе нельзя играть')

elif gamer['age'] > 90:
    question1 = input('Игра может быть сильно утомительной для вас.\nУверены ли, вы, что хотите играть?\n')

    if question1 == 'Да':
        question2 = input('Точно?\n')

        if question2 == 'Да':
            print('Хорошо, тогда начнём игру!')

        else:
            print('До свидания,', gamer['name'])

    else:
        print('До свидания,', gamer['name'])

if 18 <= gamer['age'] <= 90 or question2 == 'Да':
    print('Привет,', gamer['name'], '\nЯ могу назвать буквы алфавита, которых нет в твоем имени.')
    char = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in gamer['name']:
        if i in char:
            char = char.replace(i, '')

print('В твоём имени нет букв:')
for i in char:
    print(i)
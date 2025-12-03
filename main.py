import os
clear = lambda: os.system('cls')

words = ['кафе','зарплата','брюнет','автомобиль','звонок','бабушка','цель','жена','гражданин','театр','телевизор','хозяин','интернет','учитель']

points = {'Player 1': 0, 'Player 2': 0, 'Player 3': 0,'Player 4': 0,'Player 5': 0}

adj = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

verb = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

noun = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

number_of_players= int(input('Число игроков: '))

current_player = 0
for i in range(number_of_players):
    current_player += 1
    print('Player: ', current_player + 1)

    for j in range(3):
        adj['Player ' + str(current_player)].append(input('Введите прилагательные'))

    for j in range(3):
        verb['Player ' + str(current_player)].append(input('Введите глаголы'))

    for j in range(3):
        noun['Player ' + str(current_player)].append(input('Введите существительные'))

    clear()


#while not 15 in points.values():




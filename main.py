import os
clear = lambda: os.system('cls')

words = ['кафе','зарплата','брюнет','автомобиль','звонок','бабушка','цель','жена','гражданин','театр','телевизор','хозяин','интернет','учитель']

points = {'Player 1': 0, 'Player 2': 0, 'Player 3': 0,'Player 4': 0,'Player 5': 0}

adj = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

verb = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

noun = {'Player 1': [], 'Player 2': [], 'Player 3': [],'Player 4': [],'Player 5': []}

number_of_players= int(input('Число игроков: '))

current_player = 0
for i in range(0,number_of_players):

    print('Player: ', current_player + 1)

    for j in range(0,3):
        adj[current_player] = input('Введите прилагательные')

    for j in range(0,3):
        verb[current_player] = input('Введите глаголы')

    for j in range(0,3):
        noun[current_player] = input('Введите существительные')

#while not 15 in points.values():

clear()

print(1111)
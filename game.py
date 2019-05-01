player = {'name': 'Daniel', 'attack': 13, 'heal': 16, 'health': 100}
monster = {'name': 'Orc', 'attack': 12, 'health': 100}
game_running = True

while game_running == True:


    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    player_choice = input()


    if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']
        print(monster['health'])
        print(player['health'])

    elif player_choice == '2':
        print(player['health'] + player['heal'])

    else:
        print('Invalid Input')

    if player['health'] <= 0:
        game_running = False
        print('GAME OVER')

    elif monster['health'] <= 0:
        game_running = False
        print('YOU WIN')

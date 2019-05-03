from random import randint

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])

game_running = True


while game_running == True:
    new_round = True
    player = {'name': 'Daniel', 'attack': 13, 'heal': 16, 'health': 100}
    monster = {'name': 'Orc', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player Name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print('---' * 7)
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_choice = input()


        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True

            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            print('---' * 7)
            print('Good Bye')
            new_round = False
            game_running = False

        else:
            print('Invalid Input')

        if player_won == False and monster_won == False:
            print('---' * 7)
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print('---' * 7)
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')
            print('---' * 7)

        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print('The monster won')
            new_round = False

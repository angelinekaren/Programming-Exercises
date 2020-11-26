file = None

with open('pokemon.txt', 'r') as pokemon:
    file = pokemon.read()

word = file.split()


def play(word):
    player_turn = 0
    used_words = []
    last_word = ''
    score1 = 0
    score2 = 0
    print('Welcome to the Pokemon Game')
    print('Now, we will start the game')
    while True:

        if player_turn % 2 == 0:
            player1 = input('Player 1 = ').lower()
            if player1[0] == last_word or last_word == '' and player1 not in used_words:
                last_word = player1[-1]
                used_words.append(player1)
                player_turn += 1
                score1 += 1
            else:
                print("Word doesn't match the requirements or is used")
                if score1 > score2:
                    print('Player 1 wins with total score of', score1)
                else:
                    print('Player 2 wins with total score of', score2)
                print('Game over. Thankyou for playing.')
                print('See you next time!')
                break

        else:
            player2 = input('Player 2 = ').lower()
            if player2[0] == last_word or last_word == '' and player2 not in used_words:
                last_word = player2[-1]
                used_words.append(player2)
                player_turn += 1
                score2 += 1
            else:
                print("Word doesn't match the requirements or is used")
                if score1 > score2:
                    print('Player 1 wins with total score of', score1)
                else:
                    print('Player 2 wins with total score of', score2)
                print('Game over. Thankyou for playing.')
                print('See you next time!')
                break



if __name__ == '__main__':
    play(word)

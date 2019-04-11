#  blackjack game

import random

card_value = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,
}

def draw_card():
    card = random.choice(list(card_value.keys()))
    return card

def advice(sum):
    if sum < 17:
        return 'Hit!'
    elif (sum >= 17) and (sum < 21):
        return 'Stay!'
    elif sum == 21:
        return 'Blackjack!'
    elif sum > 21:
        return 'Busted!'


def player_hand():
    card1 = draw_card()
    card2 = draw_card()
    sum = card_value[card1] + card_value[card2]

    print(f'\nFirst Card: {card1}\nSecond Card: {card2}\n\nSum: {sum}\n{advice(sum)}\n')

    print('Choose to (hit) or (stay)')

    while True:
        if sum > 21:
            print(advice(sum))
            return sum
        choice = input('Choice: ').lower()
        if choice == 'hit':
            newcard = draw_card()
            sum += card_value[newcard]
            print(f'\nNew card: {newcard}\nSum: {sum}\n')
            print(advice(sum))
            continue
        elif choice == 'stay':
            return sum
        else:
            print('\nChoose a valid option')
            continue

def dealer_hand():
    card1 = draw_card()
    card2 = draw_card()
    sum = card_value[card1] + card_value[card2]
    print(f'Dealer First Card: {card1}\nDealer Second Card: {card2}\n\nSum: {sum}')

    while True:
        newcard = ''
        if sum < 17:
            newcard = draw_card()
            print(f'\nDealer New Card: {newcard}')
            sum += card_value[newcard]
            print(f'Dealer Sum: {sum}')
            continue
        if (sum >= 17) and (sum <= 21):
            print('\nDealer Stays')
            return sum
        else:
            print('Dealer Bust!')
            return sum

player_value = player_hand()
dealer_value = dealer_hand()

print(f'Player hand: {player_value}\nDealer hand: {dealer_value}\n')

if player_value > 21:
    print('You busted!')
elif dealer_value > 21:
    print('You win!')
elif player_value > dealer_value:
    print('You win!')
elif dealer_value > player_value:
    print('Dealer wins.')
elif dealer_value == player_value:
    print('Push')

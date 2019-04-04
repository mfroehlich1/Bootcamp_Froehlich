def pick6():
    import random
    # Return 6 random numbers in a cipher_list
    my_ticket = []
    for count in range(6):
        my_ticket.append(random.randint(1, 100))

    return my_ticket

def matches(winning_ticket, my_ticket):
    counter = 0

    for i in range(len(winning_ticket)):
        if winning_ticket[i] == my_ticket[i]:
            counter = counter + 1

    if counter == 0:
        return 0
    if counter == 1:
        return 4
    if counter == 2:
        return 7
    if counter == 3:
        return 100
    if counter == 4:
        return 50000
    if counter == 5:
        return 1000000
    if counter == 6:
        return 25000000

def play_pick6():
    spend = 0
    winnings = 0
    winning_ticket = pick6()

    for count in range(100000):
        my_ticket = pick6()
        winnings = winnings + matches(winning_ticket, my_ticket)
        spend = spend + 2

    roi = winnings - spend

    print(f"You spent ${spend}\nYou won ${winnings}\nROI = ${roi}")

play_pick6()

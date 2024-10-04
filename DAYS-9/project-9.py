print('Welcome to the secret auction program.')

def auction(bids):
    name = input('What is your name? ').lower()
    amount = int(input("What's your bid? "))
    bids[name] = amount
    return bids

def calculate_winner(bids):
    winner = []
    max_bid = 0  # Changed variable name to avoid conflict with built-in max function

    for bidder in bids:
        if bids[bidder] > max_bid:
            max_bid = bids[bidder]
            winner = [bidder]
        elif bids[bidder] == max_bid:
            winner.append(bidder)

    if len(winner) == 1:
        print(f'The winner is {winner[0]} with a bid amount of {max_bid}.')
    else:
        print(f'It is a tie! The winners are {", ".join(winner)} with a bid amount of {max_bid}.')

# Main program logic
bids = {}
is_game_on = True

while is_game_on:
    bids = auction(bids)
    check = input('Are there any other bidders? Type YES or NO: ').lower()
    if check != 'yes':
        is_game_on = False

calculate_winner(bids)

# TREASURE ISLAND

print('Welcoe to the Treasure Island')
print('Your mission is to find the treasure')

guess1 =input('You are at cross road. Where do you want to go? type left or right ').lower()

if guess1=='left':
    guess2 =input('you have come to a lake. There is an island in the middle of the lake, Type wait for a boat, type swim to swim across ').lower()
    if guess2 =='wait':
        guess3 =input('Ypu arrive at the island unharmed. There us a house with 3 doors., red, yellow, blue, choose color ').lower()

        if guess3 =='red':
            print('Burnt by fire, game over')
        elif guess3 =='yellow':
            print('Eaten by traout, game over')
        elif guess3 =='blue':
            print('YOU FOUND TREASURE')        
    else:
        print('Attacked by crocodile, game over')    
else:
    print('YOU FALL INTO HOLE')
    print('game over')    
STARTING_X = 1
STARTING_Y = 1

def north(x, y):
    if y==3:
        return False
    elif x == 2 and y == 2:
        return False
    else:
        return True 

def east(x, y):
    if y>x:
        return True
    else:
        return False

def south(x, y):
    if y == 1:
        return False
    elif x == 2 and y == 3:
        return False
    else: 
        return True

def west(x, y):
    if x != 1 and y >= x:
        return True
    else:
        return False 

def pulling_lever(coins):
    add_coins = input('Pull a lever (y/n): ')
    if add_coins == 'y' or add_coins == 'Y':
        coins += 1
        print('You received 1 coin, your total is now {}.'.format(coins))
        return coins
    elif add_coins == 'n' or add_coins == 'N':
        return coins


    
    


x = STARTING_X
y = STARTING_Y
coins = 0


while True:
    not_again = True
    print('You can travel: ', end='')
    n = north(x, y)
    e = east(x, y)
    s = south(x, y)
    w = west(x, y)
    
    if n == True and e == False and s == False and w == False:
        print('(N)orth', end='')
    if n == True and e == True and s == True and w == False:
        print('(N)orth or (E)ast or (S)outh', end='')
    if e == True and s == True and n == False and w == False:
        print('(E)ast or (S)outh', end='')
    if e == True and w == True and n == False and s == False:
        print('(E)ast or (W)est', end='')
    if s == True and w == True and n == False and e == False:
        print('(S)outh or (W)est', end='')
    if n == True and s == True and w == False and e == False:
        print('(N)orth or (S)outh', end='')        
    print('.', end='')
    print()
    direction = input('Direction: ')
    direction = direction.lower()
    if direction == 'n' or direction == 'e' or direction == 's' or direction == 'w':
        if direction == 'n' and n == True:
             y += 1
        elif direction == 'e' and e == True:
             x += 1 
        elif direction == 's' and s == True:
             y -= 1
        elif direction == 'w' and w == True:
             x -= 1
        else: 
            not_again = False
            print('Not a valid direction!')

    else:
        print('Not a valid direction!')
        not_again = False

    if not_again:
        if x == 1 and y == 2 or x == 2 and y == 2 or x == 3 and y == 2:
            coins = pulling_lever(coins)




    if x == 3 and y == 1:
        print('Victory!', end=' ')
        print('Total coins {}.'.format(coins))
        break


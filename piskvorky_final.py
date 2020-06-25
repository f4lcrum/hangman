def test(pole, coordinates):
    try:
        if int(pole[0]) > 3 or int(pole[1]) > 3:
            return 'Coordinates should be from 1 to 3!'

        ntica = (int(pole[0]), int(pole[1]))
        if coordinates[ntica] == 'X' or coordinates[ntica] == 'O':
            return "This cell is occupied! Choose another one!"

        return None

    except (IndexError, ValueError):
        return 'You should enter numbers!'

def end(coordinates):
    win_X = False
    win_O = False
    if coordinates[(1, 3)] == coordinates[(2, 2)] == coordinates[(3, 1)]:
        if coordinates[(1, 3)] == 'X':
            win_X = True
        elif coordinates[(1, 3)] == 'O':
            win_O = True

    if coordinates[(1, 1)] == coordinates[(2, 2)] == coordinates[(3, 3)]:
        if coordinates[(1, 1)] == 'X':
            win_X = True
        elif coordinates[(1, 1)] == 'O':
            win_O = True


    for i in range(3, 0, -1):
        if coordinates[(1, i)] == coordinates[(2, i)] == coordinates[(3, i)]:
            if coordinates[(1, i)] == 'X':
                win_X = True
            elif coordinates[(1, i)] == 'O':
                win_O = True

    for i in range(1, 4):
        if coordinates[(i, 3)] == coordinates[(i, 2)] == coordinates[(i, 1)]:
            if coordinates[(i, 3)] == 'X':
                win_X = True
            elif coordinates[(i, 3)] == 'O':
                win_O  = True


    if win_X:
        return 'X wins'
    elif win_O:
        return 'O wins'

    elif win_X and win_O:
        return 'impossible'
    else:
        return None


print("-"*9)
for i in range(3):
    print(f"|"+" "*7+"|")
print("-"*9)

coordinates = {(1, 3): ' ', (2, 3): ' ', (3, 3): ' ', (1, 2): ' ', (2, 2):' ',
                (3, 2):' ', (1, 1):' ', (2, 1):' ', (3, 1):' '}
coordinates_left = [(1, 3), (2, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)]


while True:
    pole_x = [i for i in input('Enter the coordinates: ').split()]
    vysl = test(pole_x, coordinates)
    while vysl and coordinates_left:
        print(vysl)
        pole_x = [i for i in input('Enter the coordinates: ').split()]
        vysl = test(pole_x, coordinates)

    ntica_X = (int(pole_x[0]), int(pole_x[1]))
    coordinates[ntica_X] = 'X'
    coordinates_left.pop(coordinates_left.index(ntica_X))


    print("-"*9)
    for x in range(3, 0, -1):
        print('| ',end='')
        for y in range(1, 3):
            print(f"{coordinates[(y, x)]} ",end='')
        print(f"{coordinates[(3, x)]} |")

    print("-"*9)

    vysl = end(coordinates)
    if vysl:
        print(vysl)
        break
    elif not vysl and not coordinates_left:
        print('Draw')
        break

    pole_O = [i for i in input('Enter the coordinates: ').split()]
    vysl = test(pole_O, coordinates)
    while vysl:
        print(vysl)
        pole_O = [i for i in input('Enter the coordinates: ').split()]
        vysl = test(pole_O, coordinates)


    ntica_O = (int(pole_O[0]), int(pole_O[1]))
    coordinates[ntica_O] = 'O'
    coordinates_left.pop(coordinates_left.index(ntica_O))

    print("-"*9)
    for x in range(3, 0, -1):
        print('| ',end='')
        for y in range(1, 3):
            print(f"{coordinates[(y, x)]} ",end='')
        print(f"{coordinates[(3, x)]} |")
    print("-"*9)


    vysl = end(coordinates)
    if vysl:
        print(vysl)
        break
    elif not vysl and not coordinates_left:
        print('Draw')
        break

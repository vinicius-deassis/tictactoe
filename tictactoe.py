from random import randint

line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]

xList = []
List0 = []

def showboard():
    print(f'   a   b   c')
    for i in range(3):
        print(f"{i}) {line1[i]} | {line2[i]} | {line3[i]}")
        print("  ___________")

def translateCoord(coordinate):
    if coordinate[0] == "a":
        return ("0",coordinate[1])
    elif coordinate[0] == "b":
        return ("1",coordinate[1])
    elif coordinate[0] == "c":
        return ("2",coordinate[1])
    else:
        print(coordinate)
        return 'wrong coordinate'

def mark(coord,symbol):
    x = coord[0]
    y = coord[1]
    if symbol == 0:
        if x == "0":
            line1[int(y)] = "O"
        elif x == "1":
            line2[int(y)] = "O"
        elif x == '2':
            line3[int(y)] = "O"
    elif symbol == 1:
        if x == "0":
            line1[int(y)] = "X"
        elif x == "1":
            line2[int(y)] = "X"
        elif x == '2':
            line3[int(y)] = "X"
    else:
        print("missing something")

def AIcoord():
    x = randint(0,2)
    y = randint(0,2)
    return (str(x), str(y))

def isMarked(coord):
    for i in xList:
        if i == coord:
            return True
    for i in List0:
        if i == coord:
            return True
    return False    

def winner(round_list):
    for i in round_list:
        for j in round_list[i]:
            

#Running
for round in range(6):
    showboard()

    answer = input("\nYou are the X, enter the coordinates: ")
    user = translateCoord(answer)
    if isMarked(user):
        print('Try again')
        continue

    mark(user, 1)
    xList.append(user)    

    showboard()

    print('\nAI MOVE\n')
    while True:
        AImove = AIcoord()
        if isMarked(AImove):
            continue
        break
    List0.append(AImove)
    mark(AImove, 0)

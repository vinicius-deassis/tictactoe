from random import randint

l1 = [" "," "," "]
l2 = [" "," "," "]
l3 = [" "," "," "]
lol = [l1,l2,l3]

xList = []
List0 = []

def showboard():
    print(f'  a   b   c')
    for i in range(3):
        print(i,end='')
        for j in range(3):
          print(f' {lol[i][j]} |', end='')
        print("\n ___________")

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
    col = coord[0]
    row = coord[1]

    if symbol == 1:
      match row:
        case "0":
          l1[int(col)] = "X"
        case "1":
          l2[int(col)] = "X"
        case "2":
          l3[int(col)] = "X"

    elif symbol == 0:
      match row:
        case "0":
          l1[int(col)] = "O"
        case "1":
          l2[int(col)] = "O"
        case "2":
          l3[int(col)] = "O"

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

def isWinner():
  #vertical
  for i in range(3):
    if l1[i] == 'X' and l2[i] =='X' and l3[i] == 'X':
      showboard()
      return True
    if l1[i] == 'O' and l2[i] =='O' and l3[i] == 'O':
      showboard()
      return True
  #horizontal
  for i in range(3):
    if lol[i][0] == 'X' and lol[i][1] == 'X' and lol[i][2] == 'X':
      showboard()
      return True
    elif lol[i][0] == 'O' and lol[i][1] == 'O' and lol[i][2] == 'O':
      showboard()
      return True
  #diagonal
  if (isMarked(('0','0')) and isMarked(('1','1')) and isMarked(('2','2'))):
    showboard()
    return True
  elif (isMarked(('0','2')) and isMarked(('1','1')) and isMarked(('2','0'))):
    showboard()
    return True

#Running
while True:
    showboard()
    #user turn
    allowed_entrys = ['a','b','c','0' ,'1' ,'2']
    answer = input("\nYou are the X, enter the coordinates (Ex.: a0): ")
    if answer == 'q':
        break

    elif not(answer[0] in allowed_entrys) or not(answer[1] in allowed_entrys):
      print('Wrong coordinate, try again.')
      continue

    user = translateCoord(answer)
    if isMarked(user):
        print('Already marked.')
        continue
    mark(user, 1)
    xList.append(user)

    if isWinner():
        print('\n You won.\n')
        break

    showboard()

    #AIturn
    print('\nAI MOVE\n')
    while True:
        AImove = AIcoord()
        if isMarked(AImove):
            continue
        break
    List0.append(AImove)
    mark(AImove, 0)

    if isWinner():
        showboard()
        print('\n AI won.\n')
        break


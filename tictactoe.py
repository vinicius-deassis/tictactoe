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
      return True
    if l1[i] == 'O' and l2[i] =='O' and l3[i] == 'O':
      return True
  #horizontal
  for i in range(3):
    if lol[i][0] == 'X' and lol[i][1] == 'X' and lol[i][2] == 'X':
      return True
    elif lol[i][0] == 'O' and lol[i][1] == 'O' and lol[i][2] == 'O':
      return True
  #diagonal
  if l1[0] == 'X' and l2[1] == 'X' and l3[2] == 'X':
    return True
  elif l1[0] == 'O' and l2[1] == 'O' and l3[2] == 'O':
    return True
  if l1[2] == 'X' and l2[1] == 'X' and l3[0] == 'X':
    return True
  elif l1[2] == 'O' and l2[1] == 'O' and l3[0] == 'O':
    return True

def checkTie():
  if len(xList) > 4:
    return True

#Running
gamemode = int(input('Choose the gamemode:\n1) Singleplayer \n2) 2 players\n'))
allowed_entrys = ['a','b','c','0' ,'1' ,'2']

if gamemode == 1:
  showboard()
  while True:
    #user turn
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
    showboard()
    xList.append(user)

    if isWinner():
      print('\n You won.\n')
      break
    
    if checkTie():
      print("\nTie!")
      break

    #AIturn
    print('\nAI MOVE\n')
    while True:
      AImove = AIcoord()
      if isMarked(AImove):
          continue
      break
    List0.append(AImove)
    mark(AImove, 0)
    showboard()

    if isWinner():
      print('\n AI won.\n')
      break

    if checkTie():
      print("\nTie!")
      break

elif gamemode == 2:
  while True:
    showboard()
    #Player 1
    player1 = input("\nYou are the X, enter the coordinates (Ex.: a0): ")
    if player1 == 'q':
      break
    elif not(player1[0] in allowed_entrys) or not(player1[1] in allowed_entrys):
      print('Wrong coordinate, try again.')
      continue

    player1 = translateCoord(player1)
    if isMarked(player1):
      print('Already marked, try again.')
      continue
    mark(player1, 1)
    showboard()
    xList.append(player1)

    if isWinner():
      print('\n X won.\n')
      break

    if checkTie():
      print("\nTie!")
      break

    #Player 2
    player2 = input("\nYou are the O, enter the coordinates (Ex.: a0): ")
    if player2 == 'q':
      break
    elif not(player2[0] in allowed_entrys) or not(player2[1] in allowed_entrys):
      print('Wrong coordinate, try again.')
      continue

    player2 = translateCoord(player2)
    if isMarked(player2):
      print('Already marked, try again.')
      continue
    mark(player2, 0)
    showboard()
    List0.append(player2)

    if isWinner():
      print('\n O won.\n')
      break

    if checkTie():
      print("\nTie!")
      break
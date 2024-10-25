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
        return coordinate.replace("a", "0")
    elif coordinate[0] == "b":
        return coordinate.replace("b", "1")
    elif coordinate[0] == "c":
        return coordinate.replace("c", "2")
    else:
        return 'wrong coordinate'

def mark(coord,symbol):
    x = coord[0]
    y = coord[1]
    if symbol == 0:
        if x == "0":
            line1[int(y)] = "0"
        elif x == "1":
            line2[int(y)] = "0"
        elif x == '2':
            line3[int(y)] = "0"
        else:
            print("wrong coordinate")
    if symbol == 1:
        if x == "0":
            line1[int(y)] = "X"
        elif x == "1":
            line2[int(y)] = "X"
        elif x == '2':
            line3[int(y)] = "X"
        else:
            print("wrong coordinate")

def IAmove():
    x = randint(0,2)
    y = randint(0,2)
    print(x,1)
    return str(x), str(y)


showboard()

asnwer = input("\nYou are the X, enter the coordinates: ")
real_answer = translateCoord(asnwer)
xList.append(real_answer)
mark(real_answer, 1)

showboard()

print('AI MOVE\n')
mark(IAmove(),0)
showboard()

#print(translateCoord(asnwer))
map = [["-","-","-"],["-","-","-"],["-","-","-"]]
c = True
def kontrol():
    if map[0][0] == map[1][0] == map[2][0] == "X" or map[0][0] == map[1][0] == map[2][0] == "O":
        print("Kazandın!")
        c = False
    elif map[0][1] == map[1][1] == map[2][1] == "X" or map[0][1] == map[1][1] == map[2][1] == "O":
        print("Kazandın!")
        c = False
    elif map[0][2] == map[1][2] == map[2][2] == "X" or map[0][2] == map[1][2] == map[2][2] == "O":
        print("Kazandın!")
        c = False
    elif map[0][0] == map[1][1] == map[2][2] == "X" or map[0][0] == map[1][1] == map[2][2] == "O":
        print("Kazandın!")
        c = False
    elif map[2][0] == map[1][1] == map[0][2] == "X" or map[2][0] == map[1][1] == map[0][2] == "O" :
        print("Kazandın!")
        c = False
    elif map[0][0] == map[0][1] == map[0][2] == "X" or map[0][0] == map[0][1] == map[0][2] == "O":
        print("Kazandın!")
        c = False
    elif map[1][0] == map[1][1] == map[1][2] == "X" or map[1][0] == map[1][1] == map[1][2] == "O":
        print("Kazandın!")
        c = False
    elif map[2][0] == map[2][1] == map[2][2] == "X" or map[2][0] == map[2][1] == map[2][2] == "O":
        print("Kazandın!")
        c = False
def Yazdir():
    for i in range(0,3):
        for k in range(0,3):
            print(map[i][k],end=" ")
        print()
    kontrol()
while c == True:
    Yazdir()
    x = int(input("X oyuncusunun yatay kordinatı : "))
    y = int(input("X oyuncusunun dusey kordinatı : "))
    map[x][y] = "X"
    Yazdir()
    a = int(input("O oyuncusunun yatay kordinatı : "))
    b = int(input("O oyuncusunun dusey kordinatı : "))
    map[a][b] = "O"

p = [
    ["" "","" "","" ""],
    ["" "","" "","" ""],
    ["" "","" "","" ""]
    ]

def rysowanie_planszy(p):
 
    w1 = p[0][0]+'|'+ p[0][1] +'|'+ p[0][2]
    w2 = p[1][0]+'|'+ p[1][1] +'|'+ p[1][2]
    w3 = p[2][0]+'|'+ p[2][1] +'|'+ p[2][2]
    w4 = '--'+'--'+'-'
    w5 = '--'+'--'+'-'

    print (w1)
    print (w4)
    print (w2)
    print (w5)
    print (w3)

rysowanie_planszy(p)

def komunikat_bledna_pozycja ():
  print ("Bledna pozycja, sprobuj jeszcze raz, good luck...")

# to kod do imienia gracza

def pobierz_imie_gracza1():
    imie = input("podaj imie gracza1 grajacego X...")
    return imie

def pobierz_imie_gracza2():
    imie = input("podaj imie gracza2 grajacego O...")
    return imie

# to kod do wypelnij pole gracza

def zamien_int_na_x_y(pozycja):
    pozycje_planszy = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
    }   
    return pozycje_planszy.get(int(pozycja), "nothing")

def pobierz_pozycje_gracza1():
    pozycja_gracza1 = input("Graczu1 gdyie stawiasz X?...")
    return zamien_int_na_x_y(pozycja_gracza1)

def pobierz_pozycje_gracza2():
    pozycja_gracza2 = input("Graczu2 gdyie stawiasz O?...")
    return zamien_int_na_x_y(pozycja_gracza2)

#print(pobierz_imie_gracza1())
#print(pobierz_imie_gracza2())
print(pobierz_pozycje_gracza1())
print(pobierz_pozycje_gracza2())
Board = [
    ['o', 'x', 'o'],
    ['x', 'o', 'x'],
    ['x', 'o', 'o'],
def Wrong_move_patt (x,y):
    if Board [x][y] != " " and Board [x][y+1] != " " and Board [x][y+2] != " " and Board[x+1][y] != " " and Board [x+1][y+1] != " " and Board [x+1][y+2] != " " and Board[x+2][y] != " " and board [x+2][y+1] != " " and Board [x+2][y+2] != " ":
def Wrong_move (x,y):
    if board[x][y]==" ":
        return True
    else:
        return False 
print(Wrong_move(1,1))


x=0
y=0
def end_of_the_game_WIN (x,y):

# Same elements in one line 

    if Board [x][y] == Board [x][y+1] and Board [x][y] == Board [x][y+2]:
        print('Bravoooo')
        return True
    else:
        print('Play')
        return False 
end_of_the_game_WIN (x,y)

# When Patt 

def Patt (x,y):
    if Board [x][y] != " " and Board [x][y+1] != " " and Board [x][y+2] != " " and Board [x+1][y] != " " and Board [x+1][y+1] != " " and Board [x+1][y+2] != " " and Board [x+2][y] != " " and \
    Board [x+2][y+1] != " " and Board [x+2][y+2] != " ":
        print("THE END")
        return True
    else:
        return False
        
Patt (x,y)
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

def komunikat_bledna_pozycja ():
  print ("Bledna pozycja, sprobuj jeszcze raz, good luck...")

def get_player_name1():
    imie = input("podaj imie gracza1 grajacego X...")
    return imie

def get_player_name2():
    imie = input("podaj imie gracza2 grajacego O...")
    return imie

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

def get_player_position1():
    pozycja_gracza1 = input("Graczu1 gdyie stawiasz X?...")
    return zamien_int_na_x_y(pozycja_gracza1)

def get_player_position2():
    pozycja_gracza2 = input("Graczu2 gdyie stawiasz O?...")
    return zamien_int_na_x_y(pozycja_gracza2)

def czy_dozwolony_ruch (x,y):
    if plansza[x][y]==" ":
        return True
    else:
        return False 

def czy_koniec_gry_zwyciestwo (x,y):
    # w lini te same znaki
    if plansza [x][y] == plansza [x][y+1] and plansza [x][y] == plansza [x][y+2]:
        print('Bravoooo')
        return True
    else:
        print('grajdalej')
        return False 

def czy_koniec_gry_patt (x,y):
    if plansza[x][y] != " " and plansza [x][y+1] != " " and plansza [x][y+2] != " " and plansza[x+1][y] != " " and plansza [x+1][y+1] != " " and plansza [x+1][y+2] != " " and plansza[x+2][y] != " " and \
       plansza [x+2][y+1] != " " and plansza [x+2][y+2] != " ":
        print("koniec gry")
        return True
    else:
        return False 

def wypelnij_pole_gracz1(x, y):
    plansza[x][y] = 'X'

def wypelnij_pole_gracz2(x ,y):
    plansza[x][y] = 'O'

def czy_koniec_gry():
    czy_koniec_gry_patt()
    czy_koniec_gry_zwyciestwo()

def main():
    get_player_name1()
    get_player_name2()
    rysowanie_planszy(p)
    print(get_player_position1())
    # czy_dozwolony_ruch()
    # czy_dozwolony_ruch(get_player_position2())
    czy_koniec_gry()

#GRAMY!!!!11111jeden :)
main()


# rysowanie_planszy(p)


# x=0
# y=0
# czy_koniec_gry_zwyciestwo (x,y)

# czy_koniec_gry_patt (x,y)  
# #print(get_player_name1())
# #print(get_player_name2())
# print(get_player_position1())
# print(get_player_position2())
# plansza = [
#     ['o', 'x', 'o'],
#     ['x', 'o', 'x'],
#     ['x', 'o', 'o'],
# ]
# print(czy_dozwolony_ruch(1,1))

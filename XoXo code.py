# https://docs.google.com/spreadsheets/d/1uQEFB-bPmcBykrD_ulPELHtcM8nPYGAB8XqgaCApPhI/edit#gid=0
p = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]

Board = [
    ['o', 'x', 'o'],
    ['x', 'o', 'x'],
    ['x', 'o', 'o'],
]

def draw_the_board(p):
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

def msg_wrong_position ():
    print ("Wrong position, try again, good luck...")

def get_player_name1():
    name = input("Player 1 What's your name (you play X):")
    return name

def get_player_name2():
    name = input("Player 1 What's your name (you play O):")
    return name

def change_int_to_x_y(positions):
    # TODO: should not accept values other than 1-9
    board_positions = {
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
    return board_positions.get(int(positions), "nothing")

def Is_it_good_move (x, y):
    if Board[x][y]==" ":
        return True
    else:
        return False 

def get_player_position1():
    # TODO fix logic
    correct_position = True
    while correct_position:
        player_position1 = input("Player 1 - where do you want to put X:")
        if player_position1.isdigit() and int(player_position1) in range(1,9):
            x, y  = change_int_to_x_y(player_position1)
            if not Is_it_good_move(x, y):
                correct_position = True
            break
        else:
            print("Wrong position. Try again")
            continue
    return change_int_to_x_y(player_position1)

def get_player_position2():
    correct_position = True
    while correct_position:
        player_position2 = input("Player 2 - where do you want to put O:")
        if player_position2.isdigit() and int(player_position2) in range(1,9):
            x, y  = change_int_to_x_y(player_position2)
            if not Is_it_good_move(x, y):
                correct_position = True
            break
        else:
            print("Wrong position. Try again")
            continue
    return change_int_to_x_y(player_position2)
x=0
y=0
# Win - Same elements in one line

def end_of_the_game_WIN (x,y):
    if Board [x][y] == "x" and Board [x][y+1] == "x" and Board [x][y+2] == "x" \
        or Board [x+1][y] == "x" and Board [x+1][y+1] == "x" and Board [x+1][y+2] == "x" \
        or Board [x+2][y] == "x" and Board [x+2][y+1] == "x" and Board [x+2][y+2] == "x" \
        or Board [x][y] == "x" and Board [x+1][y] == "x" and Board [x+2][y] == "x" \
        or Board [x+1][y] == "x" and Board [x+1][y+1] == "x" and Board [x+1][y+2] == "x" \
        or Board [x+2][y] == "x" and Board [x+2][y+1] == "x" and Board [x+2][y+2] == "x" \
        or Board [x][y] == "o" and Board [x][y+1] == "o" and Board [x][y+2] == "o" \
        or Board [x+1][y] == "o" and Board [x+1][y+1] == "o" and Board [x+1][y+2] == "o" \
        or Board [x+2][y] == "o" and Board [x+2][y+1] == "o" and Board [x+2][y+2] == "o" \
        or Board [x][y] == "o" and Board [x+1][y] == "o" and Board [x+2][y] == "o" \
        or Board [x+1][y] == "o" and Board [x+1][y+1] == "o" and Board [x+1][y+2] == "o" \
        or Board [x+2][y] == "o" and Board [x+2][y+1] == "o" and Board [x+2][y+2] == "o":
        print('Bravoooo')
        return True
    else:
        return False 

# When Patt 

def Patt (x,y):
    if Board [x][y] != " " and Board [x][y+1] != " " and Board [x][y+2] != " " and Board [x+1][y] != " " and Board [x+1][y+1] != " " and Board [x+1][y+2] != " " and Board [x+2][y] != " " and \
    Board [x+2][y+1] != " " and Board [x+2][y+2] != " ":
        print("THE END")
        return True
    else:
        return False
        

def fillout_p1(x, y):
    Board[x][y] = 'X'

def Fillout_p2(x ,y):
    Board[x][y] = 'O'

def Is_it_end():
    # TODO - add a flowchart / logic
    if Patt (x,y) or end_of_the_game_WIN (x,y):
        return True
    else:
        return False

def setup():
    get_player_name1()
    get_player_name2()
    draw_the_board(p)

def show_winner(player):
    print("the winner is ", player)

def test_drawing_board():
    p = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    draw_the_board(p)
    p[1][1] = "X"
    draw_the_board(p)

def test_Is_it_end():
    global p 
    p = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print(Is_it_end ())
    Board = [
        ["x", "x", "x"],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    print(Is_it_end ())

def test():
    test_drawing_board()
    test_Is_it_end()
    print(get_player_position1())
    print(get_player_position2())
    print(Is_it_good_move(1,1))

def main():
   
    test()
    exit()

    setup()
    while True:
        get_player_position1()

        if Is_it_end():
            show_winner("Player1")
            break

        get_player_position2()
            
        if Is_it_end():
            show_winner("Player2")
            break


main()



p_legend = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
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

draw_the_board(p_legend)

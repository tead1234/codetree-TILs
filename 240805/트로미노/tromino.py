n,m = map(int, input().split())

score_board = [list(map(int, input().split())) for _ in range(n)]

def netherland_down(start_x, start_y):
    add_x = [0, 1, 1]
    add_y = [0, 0, 1]
    validate = True
    MAX = 0
    for add in range(3):
        if 0 <= add_x[add] + start_x < n and 0<= add_y[add] + start_y < m:
            pass
        else:
            validate = False
    if validate:
        for add in range(3):
            MAX += score_board[add_x[add] + start_x][add_y[add] + start_y]
    return MAX
def netherland_left(start_x, start_y):
    add_x = [0, 0, 1]
    add_y = [0, -1, -1]
    validate = True
    MAX = 0
    for add in range(3):
        if 0 <= add_x[add] + start_x < n and 0<= add_y[add] + start_y < m:
            pass
        else:
            validate = False
    if validate:
        for add in range(3):
            MAX += score_board[add_x[add] + start_x][add_y[add] + start_y]
    return MAX
def netherland_up(start_x, start_y):
    add_x = [0, -1, -1]
    add_y = [0, 0, -1]
    validate = True
    MAX = 0
    for add in range(3):
        if 0 <= add_x[add] + start_x < n and 0<= add_y[add] + start_y < m:
            pass
        else:
            validate = False
    if validate:
        for add in range(3):
            MAX += score_board[add_x[add] + start_x][add_y[add] + start_y]
    return MAX
def netherland_right(start_x, start_y):
    add_x = [0, 0, -1]
    add_y = [0, 1, 1]
    validate = True
    MAX = 0
    for add in range(3):
        if 0 <= add_x[add] + start_x < n and 0<= add_y[add] + start_y < m:
            pass
        else:
            validate = False
    if validate:
        for add in range(3):
            MAX += score_board[add_x[add] + start_x][add_y[add] + start_y]
    return MAX
def squareShape_row(start_x, start_y):
    MAX = 0
    if 0 <= start_x + 2 < n and 0 <= start_y <m:
        save = 0
        for add in range(3):
            save += score_board[start_x + add][start_y]
        if MAX < save:
            MAX = save
    return MAX

def squareShape_line(start_x, start_y):
    MAX = 0
    if 0 <= start_x < n and 0 <= start_y + 2 <m:
        save = 0
        for add in range(3):
            save += score_board[start_x][start_y + add]
        if MAX < save:
            MAX = save
    return MAX
MAX = 0
for i in range(n):
    for j in range(m):
        answer = max(squareShape_row(i,j), squareShape_line(i,j), netherland_down(i,j), netherland_left(i,j), netherland_right(i,j), netherland_up(i,j))
        if answer > MAX:
            MAX = answer
print(MAX)
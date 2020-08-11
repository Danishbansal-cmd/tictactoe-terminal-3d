# copyright by danish bansal (Danishbansal-cmd)

board = [[['.','.','.'],
          ['.','.','.'],
          ['.','.','.']],
         [['.', '.', '.'],
          ['.', '.', '.'],
          ['.', '.', '.']],
         [['.', '.', '.'],
          ['.', '.', '.'],
          ['.', '.', '.']]]

player1 = 'x'
player2 = 'o'
score1 = 0
score2 = 0
i = 0
input1 = 30

def create_board(board):
    for i in range(3):
        for x in range(3):
            for y in range(3):
                print('{}|'.format(board[i][x][y]), end = " ")
            print()
        print()

def move(board):
    global score1,score2,count,run,input1

    list = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                i = board[x][y][z]
                list.append(i)

    os = list.count('o')
    xs = list.count('x')
    if os > xs:
        player = player1
        print('player',player,'turn')
    elif os < xs:
        player = player2
        print('player',player,'turn')
    else:
        player = player2
        print('player',player,'turn')
    if '.' not in list:
        check_score()
        print('score of player: "o": ',score2)
        print('score of player: "x": ',score1)
        if score1 > score2:
            print('player "x" wins')
        elif score2 > score1:
            print('player "o" wins')
        else:
            print('its tie')
        run = False
    else:
        input1 = int(input('Enter the number from 1-9: '))




        for count in range(27):
            if list[count] == '.' and count != 27:
                i = count // 9
                break


        if input1 == 1 and board[i][0][0] == '.':
            board[i][0][0] = player
        if input1 == 2 and board[i][0][1] == '.':
            board[i][0][1] = player
        if input1 == 3 and board[i][0][2] == '.':
            board[i][0][2] = player
        if input1 == 4 and board[i][1][0] == '.':
            board[i][1][0] = player
        if input1 == 5 and board[i][1][1] == '.':
            board[i][1][1] = player
        if input1 == 6 and board[i][1][2] == '.':
            board[i][1][2] = player
        if input1 == 7 and board[i][2][0] == '.':
            board[i][2][0] = player
        if input1 == 8 and board[i][2][1] == '.':
            board[i][2][1] = player
        if input1 == 9 and board[i][2][2] == '.':
            board[i][2][2] = player

def check_score():
    players = ['o','x']
    global score1,score2
    #winning conditions
    for player in players:
        for j in range(3):
            for x in range(3):  # horizontal win
                if board[j][x][0] == player and board[j][x][1] == player and board[j][x][2] == player:
                    if player == player1:
                        score1 += 1
                    else:
                        score2 += 1

            for x in range(3):  # vertical win
                if board[j][0][x] == player and board[j][1][x] == player and board[j][2][x] == player:
                    if player == player1:
                        score1 += 1
                    else:
                        score2 += 1
        #diagonal win
        if board[j][0][0] == player and board[j][1][1] == player and board[j][2][2] == player:
            if player == player1:
                score1 += 1
            else:
                score2 += 1
        if board[j][0][2] == player and board[j][1][1] == player and board[j][2][0] == player:
            if player == player1:
                score1 += 1
            else:
                score2 += 1

        #3d winning conditions
        #3d horizontal win
        for x in range(3):
            for y in range(3):
                if board[0][x][y] == player and board[1][x][y] == player and board[2][x][y] == player:
                    if player == player1:
                        score1 += 1
                    else:
                        score2 += 1
        for x in range(3):
            if board[0][x][0] == player and board[1][x][1] == player and board[2][x][2] == player:
                if player == player1:
                    score1 += 1
                else:
                    score2 += 1
            if board[0][x][2] == player and board[1][x][1] == player and board[2][x][0] == player:
                if player == player1:
                    score1 += 1
                else:
                    score2 += 1
            if board[0][0][x] == player and board[1][1][x] == player and board[2][2][x] == player:
                if player == player1:
                    score1 += 1
                else:
                    score2 += 1
            if board[0][2][x] == player and board[1][1][x] == player and board[2][0][x] == player:
                if player == player1:
                    score1 += 1
                else:
                    score2 += 1
        # 3d diagonal win
        if board[0][0][0] == player and board[1][1][1] == player and board[2][2][2] == player:
            if player == player1:
                score1 += 1
            else:
                score2 += 1
        if board[0][0][2] == player and board[1][1][1] == player and board[2][2][0] == player:
            if player == player1:
                score1 += 1
            else:
                score2 += 1

run = True
while run:
    create_board(board)
    move(board)
from aoc_fetcher import get_data
#f = open("Day_4_input.txt", "r")

input = get_data(2021, 4)
#input = f.read()

def check_for_winner(board):
    #rows
    return board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' and board[0][3] == 'X' and board[0][4] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' and board[1][3] == 'X' and board[1][4] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' and board[2][3] == 'X' and board[2][4] == 'X' or board[3][0] == 'X' and board[3][1] == 'X' and board[3][2] == 'X' and board[3][3] == 'X' and board[3][4] == 'X' or board[4][0] == 'X' and board[4][1] == 'X' and board[4][2] == 'X' and board[4][3] == 'X' and board[4][4] == 'X' or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' and board[3][0] == 'X' and board[4][0] == 'X' or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' and board[3][1] == 'X' and board[4][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' and board[3][2] == 'X' and board[4][2] == 'X' or board[0][3] == 'X' and board[1][3] == 'X' and board[2][3] == 'X' and board[3][3] == 'X' and board[4][3] == 'X' or board[0][4] == 'X' and board[1][4] == 'X' and board[2][4] == 'X' and board[3][4] == 'X' and board[4][4] == 'X'


def flatten(t):
    flat_list = [item for sublist in t for item in sublist]
    return flat_list


def part1():
    data = input.split("\n\n")
    drawn_numbers = data[0].split(',')
    boards = []
    print(drawn_numbers)
    for line in data[1:]:
        rows = line.split('\n')
        res = []
        for row in rows:
            res.append([row[:3:].strip(), row[3:6:].strip(), row[6:9:].strip(), row[9:12:].strip(), row[12:15:].strip()])
        boards.append(res)
    #print(boards[:5])
    winner = False
    winning_board = 0
    winning_number = 0
    counter = 0
    #print(boards[:2])
    while(len(boards) > 1):
        bingo = drawn_numbers[counter]
        print(bingo)
        for board in boards:
            print(board)
            for i in range(5):
                for j in range(5):
                    if board[i][j] == bingo:
                        board[i][j] = 'X'
                        did_win = check_for_winner(board)
                        if did_win:
                            boards.remove(board)
                            #winning_board = board
                            #winning_number = bingo
                            #winner = True
        #print(counter)
        counter += 1
        #print(boards[:3])
    #print(winning_number)
    #print(winning_board)
    #print((63+3+22+7+10+76+77+38+31+75+74+78+86+64+71+90+67) * 48)

part1()
#print(check_for_winner([['X', 'X', '31', '88', 'X'], ['29', 'X', '65', '68', '39'], ['X', 'X', 'X', '69', '22'], ['66', 'X', '18', '84', '11'], ['7', 'X', '92', '96', '99']]))

#print(5 in append, [[1,2],[3,4],[5,6],[7,8]])

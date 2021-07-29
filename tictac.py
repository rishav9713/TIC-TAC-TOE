
theBoard = {'1': " ", '2': " ", '3': " ", '4': " ", '5': " ", '6': " ", '7': " ", '8': " ", '9': " "}



def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def playGame():
    player1 = input('Enter first player name: ')
    player2 = input('Enter second player name: ')

    print(player1 + ':X' +" " + player2 + ':0')

    turn = 'X'
    count = 0

    player = player1

    while True:
        printBoard(theBoard)

        if count==9:
            print('The game is a tie!')
            break
        if player == player1:
            move = input('Enter your move {}: '.format(player1))
        else:
            move = input('Enter your move {}: '.format(player2))

        
        if move not in theBoard.keys():
            print('Please enter a valid move.')
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn

        
            winner = checkWin(turn)
            if winner!= '':
                printBoard(theBoard)
                print('Congratulation! the winner is ', player)
                print("***Wooho....You WIN!")
                break

            else:
                count+=1
                if turn == "X":
                    turn = "O"
                    player = player2
                else:
                    turn = "X"
                    player = player1
            
        else:
            print('This field alredy field')
            continue

        




def checkWin(turn):
    winner = ''

    if (theBoard['7']== theBoard['8']== theBoard['9']== turn) or (theBoard['4']== theBoard['5']== theBoard['6']== turn) or (theBoard['1']== theBoard['2']== theBoard['3']== turn):
        winner = turn
    
    if (theBoard['7']== theBoard['4']== theBoard['1']== turn) or (theBoard['8']== theBoard['5']== theBoard['2']== turn) or (theBoard['9']== theBoard['6']== theBoard['3']== turn):
        winner = turn

    if (theBoard['7']== theBoard['5']== theBoard['3']== turn) or (theBoard['9']== theBoard['5']== theBoard['1']== turn):
        winner = turn

    return winner 


def main():
    playGame()

if __name__ == "__main__":
    main()
    
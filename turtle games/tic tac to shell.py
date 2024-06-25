def game():
    board = [" "] * 9
    Winner = False
    turn = "X"

    for i in range(9):
        while 1:
            try:
                spot = int(input("It is %s's turn:" % turn)) - 1

                if 0 <= spot <= 8 and board[spot] == " ":
                    board[spot] = turn
                    break
            except:
                pass

            print("ERROR!")
        print("-" * 7)
        print("|%s|%s|%s|" % (board[0], board[1], board[2]))
        print("-" * 7)
        print("|%s|%s|%s|" % (board[3], board[4], board[5]))
        print("-" * 7)
        print("|%s|%s|%s|" % (board[6], board[7], board[8]))
        print("-" * 7)
        print(" ")
        for r in range(3):
            if board[r * 3] == board[r * 3 + 1] == board[r * 3 + 2] == turn:
                Winner = True
                break
            if board[r] == board[r + 3] == board[r + 6] == turn:
                Winner = True
                break

        if board[0] == board[4] == board[8] == turn:
            Winner = True

        if board[2] == board[4] == board[6] == turn:
            Winner = True

        if Winner:
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    if Winner:
        print("%s Wins" % (turn))
    else:
        print("cats game!")


game()

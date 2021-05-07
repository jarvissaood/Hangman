def hangman(word):
    wrong = 0
    stages = ["",
              "__________                      ",
              "|                               ",
              "|         |                     ",
              "|         0                     ",
              "|        /|\                    ",
              "|        / \                    ",
              "|                               "
              ]
    r_l = list(word)
    board = ["__"]*len(word)
    win = False
    print ("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print ("\n")
        msg = "Guess the word"
        char = input(msg)
        if char in r_l:
            cind= r_l.index(char)
            board[cind] = char
            r_l[cind] = "$"
        else:
             wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print ("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n"
                  .join(stages[0:wrong]))
            print("you loose. It was {}".format(word))

hangman("saeed")


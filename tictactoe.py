import random,sys,time
n=[j for j in range(1,10)]
board=[" " for i in range(9)]
print("TIC-TAC-TOE")
print("-----------")
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])
    print(row1)
    print("-------")
    print(row2)
    print("-------")
    print(row3)
    print("-------")
def player_move(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print("your turn player{}".format(number))
    choice1=int(input("enter your move(1-9):").strip())
    if(choice1>0 and choice1<=9):
        if(board[choice1-1]==" "):
            board[choice1-1]=icon
        else:
            print()
            print("this space was already filled :(")
            print()
            player_move(icon)
    else:
        print("Invalid move....please enter again")
        player_move(icon)
def player_commove(icon):
    n1=random.choice(n)
    print("computer turn:")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if(board[n1-1]==" "):
        board[n1-1]=icon
    else:
        print("this space is already filled :(")
        print()
        player_commove(icon)
def is_victory(icon):
    if(board[0]==board[1]==board[2]==icon or\
       board[3]==board[4]==board[5]==icon or\
       board[6]==board[7]==board[8]==icon or\
       board[0]==board[3]==board[6]==icon or\
       board[1]==board[4]==board[7]==icon or\
       board[2]==board[5]==board[8]==icon or\
       board[0]==board[4]==board[8]==icon or\
       board[2]==board[4]==board[6]==icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while(True):
    ch=int(input("mode you want to play \n 1.computer vs palyer \n 2.player vs palyer"))
    if(ch==1):
        while(True):
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("player(X) wins....Congratulations")
                sys.exit()
            elif(is_draw()):
                print("Its draw")
                sys.exit()
            player_commove("O")
            if(is_victory("O")):
                print_board()
                print("player(O) wins....Congratulations")
                sys.exit()
            elif(is_draw()):
                print("Its draw")
                sys.exit()
    elif(ch==2):
         while True:
              print_board()
              player_move("X")
              print_board()
              if is_victory("X"):
                  print("player(X) wins....Congratulations")
                  sys.exit()
              elif(is_draw()):
                  print("Its draw")
                  sys.exit()
              player_move("O")
              if(is_victory("O")):
                 print_board()
                 print("player(O) wins....Congratulations")
                 sys.exit()
              elif(is_draw()):
                  print("Its draw")
                  sys.exit()
    else:
        print("enter again")
               
                
                 












       

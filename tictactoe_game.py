import os

def draw_board(spots):
    board=(f"|{spots[1]}| {spots[2]}| {spots[3]}|\n"
           f"|{spots[4]}| {spots[5]}| {spots[6]}|\n"
           f"|{spots[7]}| {spots[8]}| {spots[9]}|")
    print(board)
spots={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
#draw_board(spots)
def check_turn(turn):
    if turn % 2 == 0: return "O"
    else: return "X"
    
def check_for_win(spots):

    ganador = False
    if (spots[1] == spots[2] == spots[3]  or 
        spots[4] == spots[5] == spots[6] 
        or spots[7] == spots[8] == spots[9]  ):
        ganador  = True 
    elif (spots[1] == spots[4] == spots[7]  or 
        spots[2] == spots[5] == spots[8] 
        or spots[3] == spots[6] == spots[9]):
        ganador =  True
    elif (spots[1] == spots[5] == spots[9]  or 
        spots[7] == spots[5] == spots[3]):
        ganador = True 

    return  ganador


playing=True
turn = 0
while playing:
    os.system("cls" if os.name =="nt" else "clear")
    draw_board(spots)
    print("Player " + str((turn %2)+1) + "'s turn:  Pick yout spot or press q to quit")
    choice = input()
    if choice == "q":
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
       
        if  spots[int(choice)] not in {"X", "O"}:
            turn += 1
            spots [int(choice)] = check_turn(turn)
    
    if check_for_win(spots) == True:
        print("Ganaste")
        playing  = False
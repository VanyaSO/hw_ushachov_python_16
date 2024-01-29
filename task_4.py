board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    for i in range(3):
        print(board[i*3], board[i*3 + 1], board[i*3 + 2])
    


def player_step(char, number):
    if board[number - 1] in ("x", "o"):
        return False
    
    board[number - 1] = char
    
    return True



def check_win():
    win = False
    
    win_combinations = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )
    
    for comb in win_combinations:
        if board[comb[0]] == board[comb[1]] == board[comb[2]]:
            win = board[comb[0]]
            return win 
        
    return win



def start_game():
    current_player = "x"
    step = 1
    
    draw_board()
    
    while (step <= 9) and (check_win() == False):
        number = input(f"Player player {current_player}. Enter one of the available numbers: ")
        
        if number.isdigit() and int(number) >= 1 and int(number) <= 9:
            
            if player_step(current_player, int(number)):
                print("The move is completed!")
                draw_board()
            else: 
                print("Move not completed!")
                continue
            
            if current_player == "x":
                current_player = "o"
            else:
                current_player = "x"
                
                
            step += 1
        
    if(check_win()):
        print(f"Win player {check_win()}")
    else:
        print("The game is a tie!")
            
            
    
start_game()
import  itertools

def game_board(game_map,player=0, row=0, col=0, just_display=False):
        if game_map[row][col] != 0:
            print("This is occupied, choose another one")
            return game_map, False
        print('   '+'  '.join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][col] = player
        for count, row in enumerate(game_map):
            print(count,row)
        #check_win(game)
        return game_map, True

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    #horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally")
            return True
    #vertical
    for col in range(len(current_game)):
        check = []
        for row in game:
            check.append(row[col]);
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically")
            return True
    #diagonal
    diags_downwards = []
    diags_upwards = []
    col_increase = range(len(current_game))
    row_decrease = reversed(range(len(current_game)))
    for ix in range(len(current_game)):
        diags_downwards.append(current_game[ix][ix])
    for a,b in zip(row_decrease,col_increase):
        diags_upwards.append(current_game[a][b])
    if all_same(diags_downwards):
            print(f"Player {diags_downwards[0]} is the winner diagonally (\\)")
            return True
    elif all_same(diags_upwards):
            print(f"Player {diags_upwards[0]} is the winner diagonally (/)")
            return True

    return False

def print_board(current_game):
    for count, row in enumerate(current_game):
            print(count,row)

def build_game(size):
    game = [[0 for i in range(size)]for i in range(size)]
    return game


play = True
players = [1,2]
while play:
    size = int(input("wt size? "))
    game = build_game(size)

    game_won = False
    game, _ = game_board(game, just_display = True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Cuurent Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("choose column: "))
            row_choice = int(input("choose row: "))
            game, played = game_board(game, current_player,row_choice,column_choice);
        
        if win(game):
            game_won = True
            again = input("Player again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == 'n':
                print("bye")
                play = False
            else:
                print("not a valid answer, bye")
                play = False        

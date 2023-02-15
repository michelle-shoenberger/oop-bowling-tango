from bowling import Game

game = Game()

players = input("Welcome to the bowling alley!\n Please enter your player names: ").split(" ")
game.add_players(*players)
game.print_current_game()

while True:
    mode = input("Ready to bowl next round? [y/n] ")

    if mode == 'y':
        game.play_next_round()
        game.print_current_game()
        lead = game.winner()
        if game.current_round == 10:
            print(f"{lead.name} wins!" if lead != "tie" else f"A tie!")
            break
        print(f"{lead.name} in the lead!" if lead != "tie" else f"A tie!")
    elif mode == 'n':
        break


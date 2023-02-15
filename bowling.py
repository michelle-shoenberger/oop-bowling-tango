from player import Player
from tabulate import tabulate

class Game:

    def __init__(self):
        self.scores = []
        self.totals = []
        self.current_round = 0
        self.players = []
        self.complete = False

    def add_players(self,*names):
        # accept any number of new names
        for name in names:
            new = Player(name)
            self.players.append(new)
            self.scores.append([])
            self.totals.append(0)
        return new

    def play_next_round(self):
        self.scores=[]
        self.totals=[]
        self.current_round += 1
        for player in self.players:
            player_scores = player.play(self.current_round) # for all rounds so far to update
            self.scores.append(player_scores)
            self.totals.append(player.total)

    def print_current_game(self):
        # create table: [Player name, Round 1, ..., Total]
        table = [['Player name'] + [f"Round {num}" for num in range(1, self.current_round+1)] + ['Total']]
        for i in range(len(self.players)):
            table.append([self.players[i].name] + self.scores[i] + [self.totals[i]])
        print(tabulate(table))

    def winner(self):
        greatest=0
        for i in range(len(self.totals)):
            if self.totals[i]> greatest:
                greatest = self.totals[i]
                idx = i
                tie = False
            elif self.totals[i] == greatest:
                tie = True
        return self.players[idx] if not tie else "tie"


    


# game = Game()
# game.add_players("Mark", "Mike")
# game.print_current_game()
# game.play_next_round()
# game.print_current_game()
# game.play_next_round()
# game.print_current_game()
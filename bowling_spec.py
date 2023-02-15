import unittest
from bowling import Game
from frame import Frame
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
  
    def test_return(self):
        """test return of function"""
        self.assertIsNotNone(self.game)

    def test_return2(self):
        """test return of Frame class"""
        self.round = Frame(2)
        self.assertIsNotNone(self.round.next)
    
    def test_return3(self):
        """test return of Player class"""
        self.player = Player(["Matt"])
        self.assertIsNotNone(self.player.play(1))

    def test_play(self):
        """test return of Game class"""
        scores = self.game.add_players("Matt")
        self.assertIsNotNone(scores)

    


if __name__ == "__main__":
  unittest.main()
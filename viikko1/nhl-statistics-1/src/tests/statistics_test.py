import unittest
from src.statistics import Statistics
from src.player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_player_existing_is_found(self):
        player = self.statistics.search("Semenko")
        self.assertIsNotNone(player)

    def test_no_player_return_none(self):
        player = self.statistics.search("OOLLLOOOOLOLO")
        self.assertIsNone(player)

    def test_team_return_right_players(self):
        players = self.statistics.team("PIT")
        self.assertListEqual(
            [player.name for player in players], 
            [player.name for player in [Player("Lemieux", "PIT", 45, 54)]]
            )

    def test_correct_top_scorers(self):
        scorers = self.statistics.top_scorers(1)
        self.assertListEqual(
            [player.name for player in scorers], 
            [player.name for player in [
                Player("Gretzky", "EDM", 35, 89),
                Player("Lemieux", "PIT", 45, 54)
                ]]
            )
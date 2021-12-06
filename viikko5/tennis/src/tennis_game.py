SCORE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}

EQUALS = {
    0: "Deuce",
    1: "Advantage player1",
    -1: "Advantage player2",
    2: "Win for player1",
    -2: "Win for player2"
}

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return SCORE[self.m_score1] + "-All"

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = min(max(self.m_score1 - self.m_score2, -2), 2)
            return EQUALS[minus_result]

        return SCORE[self.m_score1] + "-" + SCORE[self.m_score2]

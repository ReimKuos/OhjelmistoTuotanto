
class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scores_by_nationality(self, country):
        players = filter(lambda x: x.nationality == country, self.players)
        players = sorted(players, key=lambda x: x.goals + x.assists, reverse=True)
        return players
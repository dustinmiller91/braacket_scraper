from config import leagues

class Ranking:
    def __init__(self, id, name, league):
        # id taken from Braacket player page
        self.id = id
        # name is name that will display in all output formats
        self.name = name
        # league is the league the ranking is in
        self.league = league

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
NewEnglandMelee = leagues.NewEnglandMelee
WashingtonMelee = leagues.WashingtonMelee
    
FallWinter2022_NE = Ranking('7EADD432-EF78-40BD-A179-7D797CE9F37D', 'Fall 2021/Winter 2022', NewEnglandMelee)
InterRanking_NE = Ranking('7FA7ED91-C78A-4C46-914F-F8F444EBADA3', 'Inter-Ranking Period', NewEnglandMelee)

WinterSpring2022_WA = Ranking('2E2CC2DE-78E7-45FD-B127-ACEDCDF98D36', 'Winter/Spring 2022', WashingtonMelee)
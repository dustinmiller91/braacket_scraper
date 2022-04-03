from config import leagues

class Player:
    def __init__(self, id, name, league):
        # id taken from Braacket player page
        self.id = id
        # tag is name that will display in all output formats
        self.name = name
        # league is the league the player is in
        self.league = league
        
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

NewEnglandMelee = leagues.NewEnglandMelee
WashingtonMelee = leagues.WashingtonMelee

# create NE players
DrLobster = Player('6B2BEB69-DCE1-4095-BFED-4F3205CF3CDB', 'DrLobster', NewEnglandMelee)
Kalvar = Player('C2069576-DB5B-42E0-9C4B-31182802A60F', 'Kalvar', NewEnglandMelee)
Louis = Player('4C2B18BA-75A9-45ED-A8B6-8D891297E00A', 'Louis', NewEnglandMelee)

# create WA players
Graves = Player('61E2DC0D-3795-40E6-87D3-A331AC9DE4CA', 'Graves',  WashingtonMelee)
Vinodh = Player('9F2374B6-15FF-48BA-970A-34996F1CBC8A', 'Vinodh', WashingtonMelee)
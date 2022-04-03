class Player:
    def __init__(self, id, name):
        # id taken from Braacket player page
        self.id = id
        # tag is name that will display in all output formats
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

# create all players
DrLobster = Player('6B2BEB69-DCE1-4095-BFED-4F3205CF3CDB', 'DrLobster')
Kalvar = Player('C2069576-DB5B-42E0-9C4B-31182802A60F', 'Kalvar')
Louis = Player('4C2B18BA-75A9-45ED-A8B6-8D891297E00A', 'Louis')
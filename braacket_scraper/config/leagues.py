class League:
    def __init__(self, id, name):
        # id taken from Braacket player page
        self.id = id
        # name is name that will display in all output formats
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
NewEnglandMelee = League('nemelee', 'New England Melee')
WashingtonMelee = League ('wamelee', 'Official Washington Melee League')
class Ranking:
    def __init__(self, id, name):
        # id taken from Braacket player page
        self.id = id
        # name is name that will display in all output formats
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
    
FallWinter2022 = Ranking('7EADD432-EF78-40BD-A179-7D797CE9F37D', 'Fall 2021/Winter 2022')
InterRanking = Ranking('7FA7ED91-C78A-4C46-914F-F8F444EBADA3', 'Inter-Ranking Period')
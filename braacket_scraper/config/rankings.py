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
    
SpringSummer2023_NE = Ranking ('8ACA99D2-7BE4-41B9-9D20-27737A59D9F0', 'Spring 2023/Summer 2023', NewEnglandMelee)
FallWinter2023_NE = Ranking('397A6C32-BC24-4734-899A-06DAF20C96B1', 'Fall 2022/Winter 2023', NewEnglandMelee)
SpringSummer2022_NE = Ranking('A4581E34-1174-4F77-9A00-4CF0F8A133AD', 'Spring 2022/Summer 2022', NewEnglandMelee)
FallWinter2022_NE = Ranking('7EADD432-EF78-40BD-A179-7D797CE9F37D', 'Fall 2021/Winter 2022', NewEnglandMelee)
InterRanking_NE = Ranking('7FA7ED91-C78A-4C46-914F-F8F444EBADA3', 'Inter-Ranking Period', NewEnglandMelee)
FallWinter2020_NE = Ranking('191499FD-F577-49BD-B341-DE9BC22EB813', 'Fall 2019/Winter 2020', NewEnglandMelee)
SpringSummer2019_NE = Ranking('3B26CC90-A536-4F78-937D-8287D30608F3', 'Spring 2019/Summer 2019', NewEnglandMelee)
FallWinter2019_NE = Ranking('CE294EEF-A3D0-481D-A6EB-BEB8FEFF9738', 'Fall 2019/Winter 2020', NewEnglandMelee)
SpringSummer2018_NE = Ranking('4CA75C29-6660-4110-99CF-A291D0F2D62D', 'Spring 2018/Summer 2018', NewEnglandMelee)
FallWinter2018_NE = Ranking('274676F3-7928-4C9F-B1C0-7ECDD0ADE0CA', 'Fall 2017/Winter 2018', NewEnglandMelee)

Fall2019_WA = Ranking('B1916781-3D1C-4882-9D10-465D3F198D65', 'Fall 2019', WashingtonMelee)
Spring2020_WA = Ranking('A7683860-DB72-4DBA-B38E-59693D031CE6', 'Spring 2020', WashingtonMelee)
Fall2021_WA = Ranking('3DE1F13C-E80F-4D2E-AFDE-250EDCDE1E9E', 'Fall 2021', WashingtonMelee)
WinterSpring2022_WA = Ranking('2E2CC2DE-78E7-45FD-B127-ACEDCDF98D36', 'Winter/Spring 2022', WashingtonMelee)
Winter2023_WA = Ranking('3C84D4D4-14B8-4EEB-B39D-4A3DB1ECDC43', 'Winter 2023', WashingtonMelee)
Fall2023_WA = Ranking('D8BB3B92-2488-40D1-82FF-EEF577344011', 'Fall 2023', WashingtonMelee)

NE_all_seasons = [SpringSummer2023_NE, FallWinter2023_NE, SpringSummer2022_NE, FallWinter2022_NE, InterRanking_NE, FallWinter2020_NE, SpringSummer2018_NE, FallWinter2019_NE,
                  FallWinter2019_NE, SpringSummer2018_NE, FallWinter2018_NE]

WA_all_seasons = [Fall2019_WA, Spring2020_WA, Fall2021_WA, WinterSpring2022_WA,
                  Winter2023_WA, Fall2023_WA]
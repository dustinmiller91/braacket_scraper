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
AdmiralZhao = Player('2FBD0DB5-20A1-4E19-BCE7-64EA0588023A', 'Admiral Zhao', NewEnglandMelee)
Alt = Player('CE3A82DF-DDF2-4858-A007-D51F8C227CA5', 'Alt', NewEnglandMelee)
Alte = Player('56C9A7ED-BFFD-4EC2-9FDE-500290341D30', 'Alte', NewEnglandMelee)
Analog = Player('3927BB05-304F-4C60-AB08-8AEF00DC49C2', 'analog', NewEnglandMelee)
Ant = Player('8C4CE9D5-A1DA-48AE-B069-A4257F23ADB1', 'Ant', NewEnglandMelee)
Arcade = Player('42790139-FFF0-48E5-90ED-7F3500F2C805', 'Arcade', NewEnglandMelee)
Arty = Player('CEBCAD46-A933-4EA6-92F1-B9C85D5C71F2', 'Arty', NewEnglandMelee)
AwesomeVideoGames = Player('23F2D11B-9DA7-4FEB-9EC9-640EB1DA57D0', 'Awesome Video Games', NewEnglandMelee)
Bank = Player('E85EE0F4-C335-4A1C-A569-BE69C1675BAA', 'Bank', NewEnglandMelee)
BeastBoy = Player('7FA52F7A-1A24-4F38-84A8-E43D312323AF', 'BeastBoy', NewEnglandMelee)
Bekvin = Player('0ED0B111-D617-4E32-B2CA-9004A4BAAA22', 'Bekvin', NewEnglandMelee)
BLAK = Player('2328E264-DFBF-418C-970B-979F838361E2', 'BLAK', NewEnglandMelee)
Blizz = Player('4C3FC2FB-53CD-46F1-AF9F-32332D8882AC', 'Blizz', NewEnglandMelee)
Bonfire10 = Player('C9B8492C-13D2-4D31-A7ED-A79821206267', 'bonfire10', NewEnglandMelee)
BonkCushy = Player('10562558-14C6-4D76-B65C-212CE682E0F1', 'BonkCushy', NewEnglandMelee)
Clutch = Player('03C03D58-1C4F-4F2D-B1D8-BD622231E829', 'Clutch', NewEnglandMelee)
Cocoa_ = Player('2FCDB4A8-D43F-421E-B980-54F0668E6320', 'Cocoa_', NewEnglandMelee)
Conflict = Player('38A911E4-2509-47A1-8479-C9BD87DFB119', 'Conflict', NewEnglandMelee)
Coolslice = Player('583438BD-F9A1-413A-8F77-DEF3820143F0', 'Coolslice', NewEnglandMelee)
Cupofwater = Player('C8F72208-282F-4D3D-8E50-794DF3B55ECF', 'cupofwater', NewEnglandMelee)
Dad = Player('2C2FFDE9-4E62-443C-9A9E-94D7CBB4AE64', 'Dad', NewEnglandMelee)
Dour = Player('68A7DE4A-F72F-4BCC-85B8-FE64C165C291', 'Dour', NewEnglandMelee)
DrLame = Player('161B23E2-286E-427F-809F-D2F6FC60255D', 'Dr. Lame', NewEnglandMelee)
DrLobster = Player('6B2BEB69-DCE1-4095-BFED-4F3205CF3CDB', 'DrLobster', NewEnglandMelee)
Dudutsai = Player('A4CB0944-7C18-4BF6-BF2A-AAD9F55F7392', 'dudutsai', NewEnglandMelee)
Electroman = Player('BAB54F38-444F-4ADE-8D79-EC7D232D90E9', 'Electroman', NewEnglandMelee)
Ember = Player('10F61347-8632-448F-AAD5-AFB8F7F72C43', 'Ember', NewEnglandMelee)
Frosty = Player('716F783D-A4BF-4C99-96A5-56822659348B', 'Frosty', NewEnglandMelee)
Fruity = Player('30A150C5-8169-4068-98DA-996A6274E847', 'Fruity', NewEnglandMelee)
FutureShock = Player('5CD3DDFC-6380-4395-8DF7-590D498437E2', 'Future Shock', NewEnglandMelee)
Glock = Player('1FE504AF-EE8C-4426-AEDD-2EF99F053B17', 'glock in my toyota', NewEnglandMelee)
Golden = Player('CC999B81-122C-47AA-8B5A-A1FDABFEAD41', 'Golden', NewEnglandMelee)
Greenstach = Player('0267F6B4-223B-4D0D-B0AB-3B7084B37AB7', 'Greenstach', NewEnglandMelee)
Guex = Player('1AE48CD4-CCAB-4B99-8677-555C32A99A6B', 'Guex', NewEnglandMelee)
GWM420 = Player('20D39883-8B90-4E8A-9136-363E53E1CE37', 'GWM420', NewEnglandMelee)
Hexjo = Player('D663F90B-0A81-4D27-B32B-ED83F2395972', 'Hexjo', NewEnglandMelee)
Hysteric = Player('3576ECE4-EACF-4E83-995C-F40FB232EADD', 'Hysteric', NewEnglandMelee)
IOA = Player('4A825404-F98D-4AD7-A37F-44A0EB7EA62B', 'IOA', NewEnglandMelee)
JNaut = Player('1D1EEAFE-A49D-49FE-81FD-68A1D6923E8C', 'JNaut', NewEnglandMelee)
Jwilli = Player('C551AE24-9E46-491D-A256-D8B48C7A2BD6', 'Jwilli', NewEnglandMelee)
Kalvar = Player('C2069576-DB5B-42E0-9C4B-31182802A60F', 'Kalvar', NewEnglandMelee)
Keto = Player('443B05FC-FCF5-4200-AF36-BD6750498C65', 'Keto', NewEnglandMelee)
Khan = Player('1C938488-41B9-4007-81C0-E1C46E9BA742', 'Khan', NewEnglandMelee)
Kikoho = Player('27CF9E7D-F2DE-4126-B620-3D76454E463C', 'kikoho', NewEnglandMelee)
Kota = Player('4A441F9A-DE7E-4749-8E47-DFCBB388F23D', 'Kota', NewEnglandMelee)
KPeace = Player('EC6714D8-2B2B-4D90-8661-6CD2003BF31A', 'KPeace', NewEnglandMelee)
Kraft = Player('0CDB11B1-BCC3-4027-90F2-D74F1A9A5668', 'Kraft', NewEnglandMelee)
Krakhead = Player('01B96331-367C-42E4-B3A9-5198F728228D', 'Krakhead', NewEnglandMelee)
Kuni = Player('5D3BB58F-82D1-453A-8806-7BEE955C6230', 'Kuni', NewEnglandMelee)
L33b = Player('2CEACB53-351C-4697-9C94-0F08CC6B7828', 'L33b', NewEnglandMelee)
Lamdin = Player('3E5CBCCB-C3F7-4FE2-BC7F-B812DC3EE621', 'Lamdin', NewEnglandMelee)
Louis = Player('4C2B18BA-75A9-45ED-A8B6-8D891297E00A', 'Louis', NewEnglandMelee)
Makari = Player('40E8C7E0-FF26-44B7-9225-FD3D257CAC10', 'Makari', NewEnglandMelee)
Meep = Player('0C1E5B62-12A1-43FB-B6AB-B5FAB1651020', 'meep', NewEnglandMelee)
Mike = Player('AC78EC1F-AD14-4C0B-A251-65EF2666D605', 'Mike', NewEnglandMelee)
MommyDaddy = Player('745B344A-7D01-471F-BEDD-7709B8CA19D2', 'MommyDaddy', NewEnglandMelee)
MonkeyToes = Player('1787A0DC-2C4A-4E4A-9CD4-D1649E9855F9', 'MonkeyToes', NewEnglandMelee)
MrHeat = Player('C150D09C-906C-4C53-8B6F-FDD752F883A9', 'Mr. Heat', NewEnglandMelee)
Nico = Player('D4FE06C6-DA83-4CFF-957C-CBAC5C27D03C', 'Nico', NewEnglandMelee)
Nitro = Player('2678F735-C4C3-4182-8C1A-077C9F22F241', 'Nitro', NewEnglandMelee)
Omar = Player('E9CE59FB-4367-48F2-9A4B-14E8F6AD9064', 'Omar', NewEnglandMelee)
OppaAnimeStyle = Player('92FE5DC6-B76A-4D95-876E-016A84705A24', 'OppaAnimeStyle', NewEnglandMelee)
Pisces = Player('D97CF268-CA01-4ED3-92A4-01E11FF97284', 'Pisces', NewEnglandMelee)
PJ = Player('E42D8723-BEAA-45C8-AC52-ED47D5D77D3A', 'PJ', NewEnglandMelee)
Project = Player('55203EAD-758C-4892-96C4-6DF4600DC5F1', 'Project', NewEnglandMelee)
PSI = Player('3675716E-8E7E-427C-B98A-950150C5464F', 'PSI', NewEnglandMelee)
RamZ = Player('862DB628-08CB-4EA9-AB56-D6CDDD24C82E', 'RamZ', NewEnglandMelee)
Ruby = Player('C8EB8852-704C-4748-97D2-C603B41FE697', 'Ruby', NewEnglandMelee)
RyGuy = Player('4BC14931-9607-475B-BA6B-8A04F6A39A2C', 'RyGuy', NewEnglandMelee)
Saturn = Player('E19282AB-6510-4560-A925-E84BBD995D23', 'Saturn', NewEnglandMelee)
Scooby = Player('0D6F7F6C-D586-40B6-8048-E141F00D6D36', 'Scooby', NewEnglandMelee)
Shmeeli = Player('39E544D6-60EC-4243-829E-C0E017FD58DC', 'Shmeeli', NewEnglandMelee)
Silver = Player('8C9E3D8E-7DD2-4A8A-B7F3-353AD81F1C19', 'Silver', NewEnglandMelee)
Slox = Player('C712C006-2C29-4CEF-8E66-0B3B47936142', 'Slox', NewEnglandMelee)
Snakefood = Player('693510EF-985E-4B4E-8EDC-E409EF087658', 'Snakefood', NewEnglandMelee)
Spades = Player('56BFF9EB-C155-4AEB-B717-F6024B4A36F5', 'Spades', NewEnglandMelee)
Speez = Player('5D28B44A-607E-48F2-8A58-50259254DCCE', 'Speez', NewEnglandMelee)
StacysStepdad = Player('EC16A4A0-715F-4675-8C89-C60E61BE85AE', 'Stacy\'s Stepdad', NewEnglandMelee)
Stickman = Player('5A44543D-559F-40E9-AB13-4011BCBF7FC0', 'Stickman', NewEnglandMelee)
Stus = Player('E752C4F4-33FB-48B9-9F75-FABB77CB9DC9', 'Stus', NewEnglandMelee)
Sweat = Player('DF3CE0B4-0BA0-493F-99F3-879CD12469FD', 'Sweat', NewEnglandMelee)
Tarkus = Player('96AEC556-D019-4323-980A-3EBCDECE1102', 'Tarkus', NewEnglandMelee)
ThroneButt = Player('ECE509E7-81DA-4C7A-81BC-D6D652C68785', 'ThroneButt', NewEnglandMelee)
ThunderPaste = Player('E5452138-7949-4614-9F88-E30DC397357C', 'ThunderPaste', NewEnglandMelee)
Trail = Player('6AAA1597-FEE6-4283-82E7-153A64997FA9', 'Trail', NewEnglandMelee)
TwentyTwoK = Player('11CA20C1-5FDF-4A64-BC6C-0B5B91497FE7', '22K', NewEnglandMelee)
Twisty = Player('FF6DEEC7-30F3-4D9C-BD89-C44D0968033D', 'Twisty', NewEnglandMelee)
TwoCan = Player('99247341-865C-4056-8942-636C65BF0005', '2can', NewEnglandMelee)
Ubik = Player('6C4673F6-69D3-4D43-B585-DAF100BD2AE0', 'Ubik', NewEnglandMelee)
Veggietales = Player('7AA97FB5-6B21-4489-9823-EC3931625D3B', 'Veggietales', NewEnglandMelee)
Vinny = Player('39535E91-B2B7-4643-A966-C07179FA6546', 'Vinny', NewEnglandMelee)
Wang = Player('BCEF39FC-717A-4C0A-B806-F72DD38CBED3', 'wang', NewEnglandMelee)
Warmmer = Player('D861C5C8-2B42-4AB6-8649-6256E0EEF6E5', 'warmmer', NewEnglandMelee)
WeWa = Player('81951490-D13C-4CE7-B0B9-CC130ADF73CF', 'WeWa', NewEnglandMelee)
Yami = Player('726A52BC-CF5A-4F17-A5EF-4604CC318F03', 'YAMI', NewEnglandMelee)
Yasu = Player('48AB25E0-1608-447B-B5A2-655AF6014E33', 'Yasu', NewEnglandMelee)
Yifu = Player('856A527F-0BFA-4EF4-9D22-08950336DA47', 'Yifu', NewEnglandMelee)
Ymir = Player('7C7C8394-EFB5-4E3A-B137-9B96BA23FFEC', 'Ymir', NewEnglandMelee)
YoungCorgi = Player('20F78830-EF3F-4DF4-B348-EE940E764E27', 'Young Corgi', NewEnglandMelee)
Younger = Player('97D40D09-E9DF-468E-B90B-DD42CA8FA878', 'Younger', NewEnglandMelee)



# create WA players
Graves = Player('61E2DC0D-3795-40E6-87D3-A331AC9DE4CA', 'Graves',  WashingtonMelee)
Vinodh = Player('9F2374B6-15FF-48BA-970A-34996F1CBC8A', 'Vinodh', WashingtonMelee)
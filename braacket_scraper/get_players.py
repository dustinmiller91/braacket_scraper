from config import leagues
import requests
from bs4 import BeautifulSoup
import json

# I just about Washington Melee, but making sure this is usable for other leagues
all_leagues = [leagues.WashingtonMelee]

for league in all_leagues:
    # For storing player data
    players_dict = {}
    # For incrementing page number
    page_num = 1
    # Exit condition
    breaker = False

    while True:
        URL = f'https://braacket.com/league/{league.id}/player?rows=20&cols=&page={page_num}&page_cols=1&country=&game_character=&search='
        print(URL)
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, "html.parser")
        tbody = soup.find('tbody')

        # Find all <tr> tags within the <tbody>
        rows = tbody.find_all('tr')
        
        for row in rows:
            # Grab the tag and ID of each player
            links = row.find_all('a')
            for link in links:
                id = str(link.get('href')).split("/")[-1]
                tag = link.text

                # Badges and other random stuff make things weird, so we check to
                # ensure string length is that of a proper ID before adding
                if len(id) == 36:
                    # Check for duplicate player id
                    if id in players_dict.keys():
                        print(tag)
                        breaker = True
                    else:
                        print(f'{tag}: {id}')
                        players_dict[id] = tag

        # If given an out-of-range page number the website just goes to the last page, so
        # we can't just naively increment until we get an error. Instead we exit the loop
        # if we run into a duplicate player ID
        if breaker:
            break
        
        page_num += 1



    with open(f'{league.id}_players.json', 'w') as f:
        for k, v in players_dict.items():
            f.write(json.dumps({'id':k, 'tag':v})+'\n')

        # f.write(json.dumps(players_dict))


    print(len(players_dict))
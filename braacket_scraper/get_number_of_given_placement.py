import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings

players = players.NE_players

ranking = rankings.FallWinter2024_NE

players_by_num_placement = []

target_placement = 2

for player in players:
    
    URL = "https://braacket.com/league/" + player.league.id + "/player/" + player.id
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content_body")
    
    num_placement = 0
    
    if(not(results == None)):
    
        job_elements = results.find_all("div", class_="panel-body")
        for job_element in job_elements:
            section_heading = str(job_element)
            if("ellipsis" in section_heading):
                text_elements = section_heading.split()
                next = False
                for text_element in text_elements:
                    if(next):
                        placement = int(text_element)
                        if(placement == target_placement):
                            num_placement += 1
                        next = False
                    if(text_element == "class=\"text-bold\">"):
                        next = True
    print(str(player) + " " + str(num_placement))
    players_by_num_placement.append((player, num_placement))
players_by_num_placement.sort(key=lambda tup: tup[1], reverse=True)
for player_num_placement in players_by_num_placement:
    print(str(player_num_placement[0]) + " - " + str(player_num_placement[1]) + " events")

print("done")
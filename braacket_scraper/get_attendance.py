import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings

players = players.NE_players

ranking = rankings.FallWinter2024_NE

players_by_attendance = []

for player in players:
    
    URL = "https://braacket.com/league/" + player.league.id + "/player/" + player.id
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content_body")
    
    if(not(results == None)):
    
        job_elements = results.find_all("div", class_="panel-heading")
        for job_element in job_elements:
            section_heading = str(job_element)
            if("Tournaments history" in section_heading):
                section_heading = section_heading.replace(")", "")
                section_heading = section_heading.replace("(", "")
                text_elements = section_heading.split()
                num_events = int(text_elements[4])
                players_by_attendance.append((player, num_events))

players_by_attendance.sort(key=lambda tup: tup[1], reverse=True)
for player_attendance in players_by_attendance:
    print(str(player_attendance[0]) + " - " + str(player_attendance[1]) + " events")

print("done")
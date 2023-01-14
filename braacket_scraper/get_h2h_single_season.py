import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings

player1 = players.Kalvar
player2 = players.Louis

ranking = rankings.FallWinter2023_NE

if(player1.league != ranking.league or player2.league != ranking.league):
    raise Exception("One or more players leagues do not match ranking league")
URL = "https://braacket.com/league/" + player1.league.id + "/player/" + player1.id + "?ranking=" + ranking.id + "&player_hth=" + player2.id
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content_body")
job_elements = results.find_all("td", class_="text-right text-bold")

set_wins = job_elements[0].text
set_losses = job_elements[2].text

game_wins = job_elements[3].text
game_losses = job_elements[4].text

print(player1.name + " " + set_wins + " - " + set_losses + " " + player2.name)
print()
print()

URL = "https://braacket.com/league/" + player1.league.id + "/player/" + player1.id + "?ranking=" + ranking.id
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content_body")

job_elements = results.find_all("tr", class_="my-table-row-action")

for job_element in job_elements:
    
    sibling = job_element
    sibling = sibling.next_sibling
    while((len(sibling) == 1 or len(sibling) == 9)):
        if player2.name in str(sibling):
            print(" ".join(job_element.text.strip().split()))
            print(" ".join(sibling.text.strip().split()))
            print()
        sibling = sibling.next_sibling
        if(sibling == None):
            break
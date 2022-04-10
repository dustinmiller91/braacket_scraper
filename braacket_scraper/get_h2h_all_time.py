import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings
from config import leagues

player1 = players.Kalvar
player2 = players.Bonfire10

league = leagues.NewEnglandMelee

set_wins = 0
set_losses = 0

game_wins = 0
game_losses = 0

ranking_periods = rankings.NE_all_seasons if league == leagues.NewEnglandMelee else rankings.WA_all_seasons

for ranking in ranking_periods:

    if(player1.league != ranking.league or player2.league != league):
        raise Exception("One or more players leagues do not match ranking league")
    URL = "https://braacket.com/league/" + player1.league.id + "/player/" + player1.id + "?ranking=" + ranking.id + "&player_hth=" + player2.id
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content_body")
    job_elements = results.find_all("td", class_="text-right text-bold")
    
    set_wins += int(job_elements[0].text)
    set_losses += int(job_elements[2].text)
    
    if(not '%' in job_elements[3].text):
        game_wins += int(job_elements[3].text)
    game_losses += int(job_elements[4].text)
    
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
            
print()
print()            
print(player1.name + " " + str(set_wins) + " - " + str(set_losses) + " " + player2.name)
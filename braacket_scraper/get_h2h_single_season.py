import requests
from bs4 import BeautifulSoup
import players
import rankings


player1 = players.DrLobster
player2 = players.Kalvar

ranking = rankings.FallWinter2022

URL = "https://braacket.com/league/nemelee/player/" + player1.id + "?ranking=" + ranking.id + "&player_hth=" + player2.id
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content_body")
job_elements = results.find_all("td", class_="text-right text-bold")

set_wins = job_elements[0].text
set_losses = job_elements[1].text

game_wins = job_elements[3].text
game_losses = job_elements[4].text

print(player1.name + " " + set_wins + " - " + set_losses + " " + player2.name)
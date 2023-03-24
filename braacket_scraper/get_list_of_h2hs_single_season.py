import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings

player1 = players.Warmmer
opponents = [players.Kalvar, players.Kikoho, players.Bonfire10, players.Bekvin,
             players.Cupofwater, players.Golden, players.Younger, players.Trail,
             players.Shmeeli, players.Silver, players.Ember, players.AwesomeVideoGames,
             players.Arty, players.Dudutsai, players.Electroman, players.Artelind,
             players.Meep, players.DrLame, players.StacysStepdad, players.Bank,
             players.RegEx, players.Abel, players.Ant, players.Guex, players.Glock,
             players.Deadstock, players.MEAT, players.FreeSSBM, players.Nage,
             players.Raventoly, players.Ac3r, players.Coolslice, players.WeWa,
             players.Nitro, players.PSI, players.Twisty, players.Hexjo, players.FutureShock,
             players.YungHunn0, players.Loadspiller, players.PeteyWalnuts, players.Spades,
             players.Primer, players.Catfish, players.Riichi, players.Arcade, players.ETHANBURKE,
             players.TwoCan, players.IOA, players.Swampy, players.Tarchwood, players.Sweat,
             players.Hysteric, players.RyuCloud, players.ThirtyThreeToes, players.THEBEACHBOY,
             players.Alt, players.Kraft, players.Tenshi, players.ThunderPaste, players.Brub]

ranking = rankings.FallWinter2023_NE

for player2 in opponents:
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
    
    print(set_wins + " - " + set_losses, end ="\t")
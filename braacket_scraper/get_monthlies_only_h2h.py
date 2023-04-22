import requests
from bs4 import BeautifulSoup
from config import players
from config import rankings
import csv
import logging
import time

resultsList = []
headingsList = ['Players']

maxRetries = 10

players = [players.Kalvar, players.Kikoho, players. Warmmer, players.Bonfire10, players.Bekvin,
             players.Cupofwater, players.Golden, players.Younger, players.Trail,
             players.Shmeeli, players.Silver, players.Ember, players.AwesomeVideoGames,
             players.Arty, players.Dudutsai, players.Electroman]

monthlies = ["Mass Madness", "The ESG Monthly", "SSS", "Melee at Towne Parlor", 
             "HavenDash", "Waterville Smash Attack", "CT Gamercon", "Melee at the Elm",
             "King of the Cobb", "Melee at Third Place", "SmashUMA", "One Up Circuit Finals",
             "Giga HoG", "Smash the Line", "HavenShine", "NCS", "New England Melee Spartan",
             "Melee Club", "Wreck the Halls", "Bangor Comic", "New England Melee Arcadian"]

ranking = rankings.FallWinter2023_NE

for player in players:
    
    headingsList.append(player.name)
    
    playerList = [player.name]
    
    for opponent in players:
        if (player == opponent):
            playerList.append('-')
        else:
            if(player.league != ranking.league or opponent.league != ranking.league):
                raise Exception("One or more players leagues do not match ranking league")
            URL = "https://braacket.com/league/" + player.league.id + "/player/" + player.id + "?ranking=" + ranking.id
            page = requests.get(URL)
            
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find(id="content_body")
            
            job_elements = results.find_all("tr", class_="my-table-row-action")
            
            wins = 0
            losses = 0
            
            for job_element in job_elements:
                
                sibling = job_element
                sibling = sibling.next_sibling
                while((len(sibling) == 1 or len(sibling) == 9)):
                    if opponent.name in str(sibling):
                        event_name = " ".join(job_element.text.strip().split())
                        for monthly in monthlies:
                            if(monthly in event_name):
                                #print(event_name)
                                result = " ".join(sibling.text.strip().split())[0]
                                if result == 'W':
                                    wins += 1
                                elif result == 'L':
                                    losses += 1
                                #print(" ".join(sibling.text.strip().split()))
                                #print()
                                break
                    sibling = sibling.next_sibling
                    if(sibling == None):
                        break
            print(player.name + " " + str(wins) + " - " + str(losses) + " " + opponent.name)
            playerList.append(str(wins) + " - " + str(losses))
    resultsList.append(playerList)
     
resultsList.insert(0, headingsList)

numRetries = 0
csvWrite = False

while not csvWrite:

    try:
        csvFile = open("h2h_results_monthlies_only.csv", "w", newline='')

        csvWrite = True

    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        logging.exception(e)
        if numRetries > maxRetries:
            raise Exception("Exceeded maximum number of retries to access the file")
        print("Permission to access csv file denied, please close any programs with the file open")
        print("Waiting to retry write request to file")
        time.sleep(5)
        print("Retrying write request")

        numRetries += 1

        continue

csvFile.truncate(0)

with csvFile:
    csv
    writer = csv.writer(csvFile)
    writer.writerows(resultsList)
csvFile.close()

print("done")
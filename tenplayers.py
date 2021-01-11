from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = "https://en.wikipedia.org/wiki/Black_players_in_ice_hockey"

#Send get http request
page = requests.get(base_url)

print(page.status_code)

# Verify we had a successful get request
if page.status_code == requests.codes.ok:

  # Get the whole webpage in beautiful soup format
  bs = BeautifulSoup(page.text, 'lxml')


#Find something you specify in HTML 
black_hockey_players = bs.find('table', class_='wikitable').find('tbody').find_all('tr')
last_ten_players = black_hockey_players[-10:]


#Will hold our data
data = {
  'Name': [],
  'Team': [],
  'GamesPlayed': [],
  'Goals': [],
  'Assists': [],
  'Points': [],
}


player = last_ten_players[0]
#print(player)

playerchart = player.find('td')
#print(playerchart)

for x in last_ten_players:

  #Get 'Name' and save it in the data dictionary
  name = x.find('a')['title']
  if name:
    data['Name'].append(name)
  else:
    data['Name'].append('none')
  print("Player Name:" + name)

  #Get 'Team' and save it in the data dictionary
  team = x.find_all('a')[1]['title']
  if name:
    data['Team'].append(team)
  else:
    data['Team'].append('none')
  print("Team Name:" + team)

  #Get 'GamesPlayed' and save it in the data dictionary
  gamesplayed = x.find_all('td')[1].text
  if name:
    data['GamesPlayed'].append(gamesplayed)
  else:
    data['GamesPlayed'].append('none')
  #print("Games Played:" + gamesplayed)

  #Get 'Goals' and save it in the data dictionary
  goals = x.find_all('td')[2].text
  if name:
    data['Goals'].append(goals)
  else:
    data['Goals'].append('none')
  #print("Goals:" + goals)

  #Get 'Assists' and save it in the data dictionary
  assists = x.find_all('td')[3].text
  if name:
    data['Assists'].append(assists)
  else:
    data['Assists'].append('none')
  #print("Assists:" + assists)

  #Get 'Points' and save it in the data dictionary
  points = x.find_all('td')[4].text
  if name:
    data['Points'].append(points)
  else:
    data['Points'].append('none')
  #print("Points:" + points)


panda = pd.DataFrame(data, columns=['Name','Team', 'GamesPlayed', 'Goals','Assists','Points'])
panda.index = panda.index + 1
print(panda)
panda.to_csv('black_hockey_players.csv', sep=',', index=False, encoding='utf-8')

#Solution for the Unites States as name.  Don't do a for loop just grab each indivig

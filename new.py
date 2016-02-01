import os
import numpy as np
import requests
import time
import urllib.request
import lxml.html
team=['ATL','BKN','BOS','CHA','CHI','CLE','DAL','DEN','DET','GSW','HOU', 'IND','LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN','NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR','SAC','SAS`', 'TOR', 'UTA', 'WAS']
foo=input('Type the date of NBA information you want to see, in a 8 digits format, for example :20160108 or 20150729, followed by [ENTER]:')
tq=urllib.request.urlopen('http://www.nba.com/gameline/'+foo+'/')
teq=tq.read()
qq=teq.split()
main=list()
for i in range(len(qq)):
    if 'tricodes' in str(qq[i]):
        main.append(str(qq[i]))

mainn=list()
for i in range(len(main)):
    mainn.append(main[i].split('"')[1])

mai=list()
for i in range(len(mainn)):
    if mainn[i][0:2] in team:
        if mainn[i][0:3] not in team:
            mai.append(mainn[i][0:2])
            mai.append(mainn[i][2:])
    if mainn[i][0:3] in team:
        if mainn[i][0:2] not in team:
            mai.append(mainn[i][0:3])
            mai.append(mainn[i][3:])

print('The following teams played on the selected date:')
f=set(mai)
f=list(f)
for i in range(len(f)):
    print(f[i])

ma=set(mainn)
ma=list(ma)
print('All the matches on the selected teams are:')
for i in range(len(ma)):
    print(ma[i][0:3]+'vs'+ma[i][3:])
    
te=input('Please type a team you would like to see above, please input three capital letters as team names,like GSW,followed by [Enter]:')

for i in range(len(ma)):
    if te == ma[i][0:3] or te== ma[i][3:]:
        target=ma[i]

print('The team you select has following players:')

response=requests.get('http://espn.go.com/nba/team/roster/_/name/'+te)
htm=lxml.html.fromstring(response.text)
cr=[]
for td in htm.xpath("""//td[@class="sortcell"]"""):
     cr.append(td.text_content())

for i in range(len(cr)):
    print(cr[i])

player=input('Please type a name of player you would like to see above,for example Dwight Howard,followed by [Enter]:')
player=player.split()[1]

for i in range(len(mainn)):
    if te in mainn[i]:
        tq=mainn[i]

response=requests.get('http://www.nba.com/games/'+foo+'/'+tq+'/gameinfo.html?ls=iref:nba:scoreboard')
htm=lxml.html.fromstring(response.text)
cr=[]
for td in htm.xpath("""//td[@class="nbaGIPbPRgt"]"""):
    cr.append(td.text_content())

for td in htm.xpath("""//td[@class="nbaGIPbPRgtScore"]"""):
    cr.append(td.text_content())

for td in htm.xpath("""//td[@class="nbaGIPbPLftScore"]"""):
    cr.append(td.text_content())

for td in htm.xpath("""//td[@class="nbaGIPbPLft"]"""):
    cr.append(td.text_content())

for i in range(len(cr)):
    if player in cr[i]:
        print(cr[i])

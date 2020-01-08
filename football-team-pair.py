import pandas as pd
from pandas import DataFrame
import random
import time
import sys

teamdata = pd.read_csv("team-data.csv", sep=',')
teamdata['total'] = teamdata['skill'] + teamdata['physical'] + teamdata['intellectual'] + teamdata['defence']

teamdata.sort_values(by=['total','intellectual','defence'], ascending=False, inplace=True)
#print(teamdata)
footballteam = []
footballteampair = []
footballpoint = {}
for row in range(len(teamdata)):
    if teamdata.iloc[row,1]:
        player ={teamdata.iloc[row,0]: teamdata.iloc[row,6]}
        footballpoint[teamdata.iloc[row,0]] = teamdata.iloc[row,6]
        footballteam.append(teamdata.iloc[row,0])

#print(footballpoint)
#print(footballteam)

if len(footballteam) % 2 == 1:
    footballteam.append(" ")
    footballpoint[" "] = 0

#make pair
numplayer = len(footballteam)
i=0
while(i<numplayer):
    pair = [footballteam[i], footballteam[i+1]]
    footballteampair.append(pair)
    i+=2

#print(footballteampair)

def CheckTeam(mem1, mem2, footballteampair):
    Team1 = []
    Team2 = []
    for pair in footballteampair:
        Team1.append(pair[0])
        Team2.append(pair[1])
    if (mem1 in Team1 and mem2 in Team1) or (mem1 in Team2 and mem2 in Team2):
        return True
    else:
        return False


def calculate_rate(footballteampair, footballpoint):
    point_team1 = 0
    point_team2 = 0
    for mem in footballteampair:
        point_team1+= footballpoint.get(str(mem[0]))
        point_team2+= footballpoint.get(str(mem[1]))
    rate1 = point_team1/(point_team1+point_team2)*100
    rate2 = point_team2/(point_team1+point_team2)*100
    return [rate1, rate2] 

Stop = False
while not Stop:
    random.shuffle(footballteampair)
    random.shuffle(footballteampair)
    for pair in footballteampair:
        random.shuffle(pair)
    rate = calculate_rate(footballteampair, footballpoint)
    sys.stdout.write("--FOOTBALL TEAM PAIR--\n")
    sys.stdout.write("Waiting for random ")
    for i in range(10):
        sys.stdout.write(".")
        time.sleep(0.5)
    sys.stdout.write("\n")
    sys.stdout.write("|%3s |%10s |%10s| \n" % ("STT", "Team 1", "Team 2"))
    for i in range(29):
        sys.stdout.write("-")
        time.sleep(0.2)
    sys.stdout.write("\n")
    
    for pair in footballteampair:
        sys.stdout.write("|%3d |%10s |%10s| \n" % (footballteampair.index(pair)+1, pair[0], pair[1]))
        for i in range(29):
            sys.stdout.write("-")
            time.sleep(0.2)
        sys.stdout.write("\n")
    rate = calculate_rate(footballteampair, footballpoint)
    sys.stdout.write("|%4s: %10.2f|%10.2f| \n" % ("rate", rate[0], rate[1]))

    again = input("Are you OK? [Yes/No]:  ").lower()
    while again not in ["y", "n", "yes", "no"]:
        again = input("Make team again? [Yes/No]:  ")
    if again not in ["y", "yes"]:
        Stop = False
    else:
        Stop = True
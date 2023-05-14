from cmath import e
import requests
from random import *
import math
import pprint 
pp = pprint.PrettyPrinter(indent=0)

# team1 = input()
# team2 = input()
# team1 = "Barcelona Warriors"
# team2 = "Amsterdam Astronauts"

# team1 = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1M2id6-YABhB1ea6Uy3xad9KttCUKqlSg66YjvRma2Kg/values/{team1}!A2:G?key=AIzaSyCyE0J97OKvHRbhWatfQQ9YI6HlR-Z8qDg").json()['values']
# team2 = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1M2id6-YABhB1ea6Uy3xad9KttCUKqlSg66YjvRma2Kg/values/{team2}!A2:G?key=AIzaSyCyE0J97OKvHRbhWatfQQ9YI6HlR-Z8qDg").json()['values']
team1players = [['Josiah', 'Nzinga', 'QB', '23', '85', '0', '0'], ['Dwayne', 'Wells', 'QB', '22', '74', '0', '0'], ['Khalid', 'Musa', 'RB', '24', '90', '0', '0'], ['Jeremy', 'Walker', 'RB', '24', '80', '0', '0'], ['Jaheem', 'Turner', 'WR', '24', '90', '0', '0'], ['Jerry', 'Pringle Jr.', 'WR', '26', '89', '0', '0'], ['Jake', 'Deli', 'WR', '19', '78', '0', '0'], ['Lardo', 'Brown', 'OT', '23', '92', '0', '0'], ['Marvin', 'Mintz', 'OT', '23', '76', '0', '0'], ['Jerry', 'Cook', 'IDL', '23', '76', '0', '0'], ['Michael', 'Walker', 'IDL', '23', '70', '0', '0'], ['Berry', 'Razoe', 'IDL', '22', '69', '0', '0'], ['Luke', 'Castle III', 'ED (LB)', '27', '99', '0', '0'], ['Letavious', 'Ball', 'ED', '22', '80', '0', '0'], ['Tampa', 'Graham', 'ED', '22', '73', '0', '0'], ['Trey', 'Matthews', 'LB', '22', '78', '0', '0'], ['Corbin', 'Fulton Jr.', 'CB', '26', '94', '0', '0'], ['Dick', 'Sanders', 'S', '23', '86', '0', '0'], ['Aaron', 'Ramsdale', 'K (P)', '27', '71', '0', '0']]
team2players = [['Johnny', 'Manziel Jr.', 'QB', '22', '85', '0', '0'], ['Gio', 'Diaz', 'RB', '22', '77', '0', '0'], ['Murgen', 'Friman', 'WR', '22', '79', '0', '0'], ['Christian', 'Cash', 'WR', '22', '79', '0', '0'], ['George', 'Pickens Jr.', 'WR', '22', '75', '0', '0'], ['Max', 'Hawkins', 'TE', '24', '67', '0', '0'], ['Boron', 'Reed', 'IDL', '24', '90', '0', '0'], ["D'Brickashaw", 'Brickman Jr.', 'IDL', '23', '84', '0', '0'], ['Manuel', 'Combs', 'ED', '24', '87', '0', '0'], ['Archibaldo', 'Nino VI', 'ED', '22', '74', '0', '0'], ['Emily', 'Schromm', 'LB', '25', '82', '0', '0'], ['Orlando', 'Hawkins', 'LB', '25', '72', '0', '0'], ['Deuce', 'Sanders', 'CB', '21', '81', '0', '0'], ['Uno', 'Jones', 'CB', '23', '81', '0', '0'], ['Svetlana', 'Shusterman', 'S', '25', '77', '0', '0'], ['Walker', 'Zimmerman', 'S', '25', '67', '0', '0'], ['Bigfoot', 'Walker', 'K', '25', '71', '0', '0'], ['Chauncey', "O'Brien", 'P (K)', '24', '69', '0', '0']]
playerAttributes = [
    [
      "Johnny",
      "Manziel Jr.",
      "QB",
      "0",
      "0",
      "0",
      "0",
      "0",
      "QB"
    ],
    [
      "Gio",
      "Diaz",
      "RB",
      "0",
      "0",
      "100",
      "18",
      "0",
      "RB"
    ],
    [
      "Murgen",
      "Friman",
      "WR",
      "0",
      "0",
      "0",
      "26",
      "0",
      "WR"
    ],
    [
      "Christian",
      "Cash",
      "WR",
      "0",
      "0",
      "0",
      "19",
      "0",
      "WR"
    ],
    [
      "George",
      "Pickens Jr.",
      "WR",
      "0",
      "0",
      "0",
      "10",
      "0",
      "WR"
    ],
    [
      "Max",
      "Hawkins",
      "TE",
      "0",
      "0",
      "0",
      "21",
      "0",
      "TE"
    ],
    [
      "Boron",
      "Reed",
      "IDL",
      "0",
      "100",
      "0",
      "0",
      "0",
      "IDL"
    ],
    [
      "D'Brickashaw",
      "Brickman Jr.",
      "IDL",
      "0",
      "100",
      "0",
      "0",
      "0",
      "IDL"
    ],
    [
      "Manuel",
      "Combs",
      "ED",
      "0",
      "100",
      "0",
      "0",
      "0",
      "ED"
    ],
    [
      "Archibaldo",
      "Nino VI",
      "ED",
      "0",
      "100",
      "0",
      "0",
      "0",
      "ED"
    ],
    [
      "Emily",
      "Schromm",
      "LB",
      "0",
      "20",
      "0",
      "0",
      "50",
      "ILB"
    ],
    [
      "Orlando",
      "Hawkins",
      "LB",
      "0",
      "20",
      "0",
      "0",
      "50",
      "ILB"
    ],
    [
      "Deuce",
      "Sanders",
      "CB",
      "0",
      "5",
      "0",
      "0",
      "95",
      "CB"
    ],
    [
      "Uno",
      "Jones",
      "CB",
      "0",
      "5",
      "0",
      "0",
      "95",
      "CB"
    ],
    [
      "Svetlana",
      "Shusterman",
      "S",
      "0",
      "5",
      "0",
      "0",
      "85",
      "S"
    ],
    [
      "Walker",
      "Zimmerman",
      "S",
      "0",
      "5",
      "0",
      "0",
      "85",
      "S"
    ],
    [
      "Bigfoot",
      "Walker",
      "K",
      "0",
      "0",
      "0",
      "0",
      "0",
      "K"
    ],
    [
      "Chauncey",
      "O'Brien",
      "P (K)",
      "0",
      "0",
      "0",
      "0",
      "0",
      "P"
    ],
    [
      "Josiah",
      "Nzinga",
      "QB",
      "0",
      "0",
      "0",
      "0",
      "0",
      "QB"
    ],
    [
      "Dwayne",
      "Wells",
      "QB",
      "0",
      "0",
      "0",
      "0",
      "0",
      "QB"
    ],
    [
      "Khalid",
      "Musa",
      "RB",
      "0",
      "0",
      "80",
      "14",
      "0",
      "RB"
    ],
    [
      "Jeremy",
      "Walker",
      "RB",
      "0",
      "0",
      "20",
      "8",
      "0",
      "RB"
    ],
    [
      "Jaheem",
      "Turner",
      "WR",
      "0",
      "0",
      "0",
      "26",
      "0",
      "WR"
    ],
    [
      "Jerry",
      "Pringle Jr.",
      "WR",
      "0",
      "0",
      "0",
      "19",
      "0",
      "WR"
    ],
    [
      "Jake",
      "Deli",
      "WR",
      "0",
      "0",
      "0",
      "13",
      "0",
      "WR"
    ],
    [
      "Lardo",
      "Brown",
      "OT",
      "0",
      "0",
      "0",
      "0",
      "0",
      "OT"
    ],
    [
      "Marvin",
      "Mintz",
      "OT",
      "0",
      "0",
      "0",
      "0",
      "0",
      "OT"
    ],
    [
      "Jerry",
      "Cook",
      "IDL",
      "0",
      "100",
      "0",
      "0",
      "0",
      "IDL"
    ],
    [
      "Michael",
      "Walker",
      "IDL",
      "0",
      "100",
      "0",
      "0",
      "0",
      "IDL"
    ],
    [
      "Berry",
      "Razoe",
      "IDL",
      "0",
      "100",
      "0",
      "0",
      "0",
      "IDL"
    ],
    [
      "Luke",
      "Castle III",
      "ED (LB)",
      "0",
      "100",
      "0",
      "0",
      "0",
      "ED"
    ],
    [
      "Letavious",
      "Ball",
      "ED",
      "0",
      "100",
      "0",
      "0",
      "0",
      "ED"
    ],
    [
      "Tampa",
      "Graham",
      "ED",
      "0",
      "100",
      "0",
      "0",
      "0",
      "ED"
    ],
    [
      "Trey",
      "Matthews",
      "LB",
      "0",
      "20",
      "0",
      "0",
      "50",
      "OLB"
    ],
    [
      "Corbin",
      "Fulton Jr.",
      "CB",
      "0",
      "5",
      "0",
      "0",
      "95",
      "CB"
    ],
    [
      "Dick",
      "Sanders",
      "S",
      "0",
      "5",
      "0",
      "0",
      "85",
      "S"
    ],
    [
      "Aaron",
      "Ramsdale",
      "K (P)",
      "0",
      "0",
      "0",
      "0",
      "0",
      "K"
    ]
  ]

delete = []
for player in team1players:
    if player[4] == 'Coach':
        delete.append(player)
for player in delete:
    team1players.remove(player)

delete = []
for player in team2players:
    if player[4] == 'Coach':
        delete.append(player)
for player in delete:
    team2players.remove(player)


team1 = {
    'name' : 'Warriors',
    'pd' : 1,
    'pr' : 1,
    'rd' : 1,
    'qb' : 0,
    'k' : 18,
    'p' : 18,
    'kmin' : 0,
    'kmax' : 40,
    'kmult' : 1,
    'pmult' : 1,
    'players' : []
}
team2 = {
    'name' : 'Astronauts',
    'pd' : 1,
    'pr' : 1,
    'rd' : 1,
    'qb' : 0,
    'k' : 16,
    'p' : 17,
    'kmin' : 0,
    'kmax' : 40,
    'kmult' : 1,
    'pmult' : 1,
    'players' : []
}
teams = [team1, team2]
playerStats = [{}, {}] # 0 attempts, 1 completions, 2 passing yards, 3 passing tds, 4 passing ints, 5 carries, 6 rushing yards, 7 rushing tds, 8 receptions, 9 rec yards, 10 rec tds, 11 tfls, 12 sacks, 13 ffs, 14 frs, 15 defs, 16 ints

qbname = input(f'What is the name of {team1["name"]} QB?')
kname = input(f'What is the name of {team1["name"]} K?')
pname = input(f'What is the name of {team1["name"]} P?')

for player in team1players:
    if player[0] + player[1] == qbname:
        team1['qb'] = team1players.index(player)
    if player[0] + player[1] == kname:
        team1['k'] = team1players.index(player)
    if player[0] + player[1] == pname:
        team1['p'] = team1players.index(player)

    for k in playerAttributes:
        if k[0] == player[0] and k[1] == player[1]:
            attributes = k
            break

    team1['players'].append({
        'name' : f'{player[0]} {player[1]}',
        'ovr' : int(player[4]) + int(attributes[3]),
        'run' : int(attributes[5]) / 1,
        'passrush' : int(attributes[4]) / 1,
        'target' : int(attributes[6]),
        'coverage' : int(attributes[7]) / 1,
        'group' : attributes[8]
    })

qbname = input(f'What is the name of {team2["name"]} QB?')
kname = input(f'What is the name of {team2["name"]} K?')
pname = input(f'What is the name of {team2["name"]} P?')

for player in team2players:
    if player[0] + player[1] == qbname:
        team2['qb'] = team1players.index(player)
    if player[0] + player[1] == kname:
        team2['k'] = team1players.index(player)
    if player[0] + player[1] == pname:
        team2['p'] = team1players.index(player)

    for k in playerAttributes:
        if k[0] == player[0] and k[1] == player[1]:
            attributes = k
            break

    team2['players'].append({
        'name' : f'{player[0]} {player[1]}',
        'ovr' : int(player[4]) + int(attributes[3]),
        'run' : int(attributes[5]) / 100,
        'passrush' : int(attributes[4]) / 100,
        'target' : int(attributes[6]),
        'coverage' : int(attributes[7]) / 100,
        'group' : attributes[8]
    })

stats = {
    'totalYards' : 0,
    'totalRushYards' : 0,
    'totalPassYards' : 0,
    'totalPlays' : 0,
    'totalRuns' : 0,
    'totalPasses' : 0,
    'totalPoss' : 1,
    'totalSacks' : 0,
    'totalInts' : 0,
    'totalDefs' : 0,
    'totalIncompletes' : 0
}

# team1 = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1M2id6-YABhB1ea6Uy3xad9KttCUKqlSg66YjvRma2Kg/values/{team1}!A2:G?key=AIzaSyCyE0J97OKvHRbhWatfQQ9YI6HlR-Z8qDg").json()['values']
# team2 = requests.get(f"https://sheets.googleapis.com/v4/spreadsheets/1M2id6-YABhB1ea6Uy3xad9KttCUKqlSg66YjvRma2Kg/values/{team2}!A2:G?key=AIzaSyCyE0J97OKvHRbhWatfQQ9YI6HlR-Z8qDg").json()['values']

# nzinGA 90 manziel 83

def play(team, i, down, distance, length, last, score):
    if i == 0:
        otheri = 1
        other = team2
    else:
        other = team1
        otheri = 0

    playcalls = [[40, 60, 50, 75], [40, 46, 66, 64], [64, 87, 98, 85], [66, 100, 100, 100]]
    if distance <= 3:
        dist = 0
    elif distance <= 7:
        dist = 1
    elif distance <= 10:
        dist = 2
    else:
        dist = 3
    call = playcalls[down - 1][dist]
    if last == 'Pass' and call < 100:
        call -= 20
    if last == 'Run':
        call += 20
    rand = randint(1, 100)
    if rand > call:
        isPass = False
        isRun = True
        last = 'Run'
    else:
        isPass = True
        isRun = False
        last = 'Pass'

    #58% average pass to run

    tackle = True
    # tacklePcts = {
    #     'ED' : 12 - ((0.067 * other['pr']) * 12),
    #     'IDL' : 11.2 + (((0.067 * other['pr']) * 12) / 5),
    #     'ILB' : 22 + (((0.067 * other['pr']) * 12) / 5),
    #     'OLB' : 16.2 + (((0.067 * other['pr']) * 12) / 5),
    #     'CB' : 18.6 + (((0.067 * other['pr']) * 12) / 5),
    #     'S' : 20 + (((0.067 * other['pr']) * 12) / 5)
    # }
    tacklePcts = {
        'ED' : 12,
        'IDL' : 11.2,
        'ILB' : 22,
        'OLB' : 16.2,
        'CB' : 18.6,
        'S' : 20
    }
    tackleChoices = []
    for player in other['players']:
        tacklePct = 0 if player['group'] not in tacklePcts else tacklePcts[player['group']]
        for x in range(round((player['ovr'] - 50) * tacklePct)):
            tackleChoices.append(player['name'])
    tackler = choice(tackleChoices)

    if isPass:
        qb = team['players'][team['qb']]['name']
        pressureResult = pressure(team, other)
        if pressureResult[0] == True:
            stats['totalPlays'] += 1
            stats['totalYards'] -= pressureResult[2]
            stats['totalSacks'] += 1
            playerStats[otheri][pressureResult[3]] = playerStats[otheri].get(pressureResult[3], {})
            playerStats[otheri][pressureResult[3]]['sacks'] = playerStats[otheri][pressureResult[3]].get('sacks', 0) + 1
            tackler = pressureResult[3]
            playerStats[otheri][tackler] = playerStats[otheri].get(tackler, {})
            playerStats[otheri][tackler]['tackles'] = playerStats[otheri][tackler].get('tackles', 0) + 1
            print(f'{qb} sacked by {pressureResult[3]} for a {pressureResult[2]} yard loss')
            return [False, -1 * pressureResult[2], last] # turnover, yards gained (lost)
        
        passResult = passPlay(team, other, pressureResult[1], None, down, distance, length)
        if passResult[0] == True:
            stats['totalPlays'] += 1
            stats['totalYards'] += passResult[4]
            stats['totalPasses'] += 1
            stats['totalPassYards'] += passResult[4]
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['passyards'] = playerStats[i][qb].get('passyards', 0) + passResult[4]
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['attempts'] = playerStats[i][qb].get('attempts', 0) + 1
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['completions'] = playerStats[i][qb].get('completions', 0) + 1
            playerStats[i][passResult[5]] = playerStats[i].get(passResult[5], {})
            playerStats[i][passResult[5]]['recyards'] = playerStats[i][passResult[5]].get('recyards', 0) + passResult[4]
            playerStats[i][passResult[5]] = playerStats[i].get(passResult[5], {})
            playerStats[i][passResult[5]]['receptions'] = playerStats[i][passResult[5]].get('receptions', 0) + 1
            if length - passResult[4] <= 0:
                playerStats[i][qb] = playerStats[i].get(qb, {})
                playerStats[i][qb]['passtds'] = playerStats[i][qb].get('passtds', 0) + 1
                playerStats[i][passResult[5]] = playerStats[i].get(passResult[5], {})
                playerStats[i][passResult[5]]['rectds'] = playerStats[i][passResult[5]].get('rectds', 0) + 1
                score[i] += 7
                print(f'{qb} {passResult[4]} yard pass to {passResult[5]} for a touchdown ({score[0]}-{score[1]})')
            else:
                print(f'{qb} {passResult[4]} yard pass to {passResult[5]}')
                playerStats[otheri][tackler] = playerStats[otheri].get(tackler, {})
                playerStats[otheri][tackler]['tackles'] = playerStats[otheri][tackler].get('tackles', 0) + 1
            return [False, passResult[4], last]
        elif passResult[1] == True:
            stats['totalPlays'] += 1
            stats['totalPasses'] += 1
            stats['totalDefs'] += 1
            stats['totalIncompletes'] += 1
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['attempts'] = playerStats[i][qb].get('attempts', 0) + 1
            playerStats[i][passResult[4]] = playerStats[i].get(passResult[4], {})
            playerStats[i][passResult[4]]['defs'] = playerStats[i][passResult[4]].get('defs', 0) + 1
            print(f'{qb} pass deflected by {passResult[4]}')
            return [False, 0, last]
        elif passResult[2] == True:
            stats['totalPlays'] += 1
            stats['totalPasses'] += 1
            stats['totalInts'] += 1
            stats['totalIncompletes'] += 1
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['attempts'] = playerStats[i][qb].get('attempts', 0) + 1
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['passints'] = playerStats[i][qb].get('passints', 0) + 1
            playerStats[i][passResult[4]] = playerStats[i].get(passResult[4], {})
            playerStats[i][passResult[4]]['ints'] = playerStats[i][passResult[4]].get('ints', 0) + 1
            print(f'{qb} pass intercepted by {passResult[4]}')
            return [True, 0, last]
        elif passResult[3] == True:
            stats['totalPlays'] += 1
            stats['totalPasses'] += 1
            stats['totalIncompletes'] += 1
            playerStats[i][qb] = playerStats[i].get(qb, {})
            playerStats[i][qb]['attempts'] = playerStats[i][qb].get('attempts', 0) + 1
            print(f'{qb} pass incomplete')
            return [False, 0, last]
    
    else:
        runResult = runPlay(team, other, None, dist, length)
        stats['totalPlays'] += 1
        stats['totalYards'] += runResult[0]
        stats['totalRushYards'] += runResult[0]
        stats['totalRuns'] += 1
        playerStats[i][runResult[1]] = playerStats[i].get(runResult[1], {})
        playerStats[i][runResult[1]]['carries'] = playerStats[i][runResult[1]].get('carries', 0) + 1
        playerStats[i][runResult[1]] = playerStats[i].get(runResult[1], {})
        playerStats[i][runResult[1]]['rushyards'] = playerStats[i][runResult[1]].get('rushyards', 0) + runResult[0]
        tflPcts = {
            'ED' : 42,
            'IDL' : 25,
            'ILB' : 5,
            'OLB' : 15,
            'CB' : 5,
            'S' : 8
        }
        if runResult[0] < 0:
            tflChoices = []
            for player in other['players']:
                tflPct = 0 if player['group'] not in tflPcts else tflPcts[player['group']]
                for x in range(round((player['ovr'] - 50) * tflPct)):
                    tflChoices.append(player['name'])
            tackler = choice(tflChoices)
            playerStats[otheri][tackler] = playerStats[otheri].get(tackler, {})
            playerStats[otheri][tackler]['tfls'] = playerStats[otheri][tackler].get('tfls', 0) + 1
            print(f'{runResult[1]} {runResult[0]} yard run')
        elif length - runResult[0] <= 0:
            playerStats[i][runResult[1]] = playerStats[i].get(runResult[1], {})
            playerStats[i][runResult[1]]['rushtds'] = playerStats[i][runResult[1]].get('rushtds', 0) + 1
            score[i] += 7
            print(f'{runResult[1]} {runResult[0]} yard run for a touchdown ({score[0]}-{score[1]})')
        else:
            playerStats[otheri][tackler] = playerStats[otheri].get(tackler, {})
            playerStats[otheri][tackler]['tackles'] = playerStats[otheri][tackler].get('tackles', 0) + 1
        return [False, runResult[0], last]


def pressure(team, other): # 9.8% average pass rush win rate 68.3% chance to sack when you pressure 32.6% average team pressure rate 6.7% average team sack rate
    rand = randint(1, 1000)
    pressureRate = int(326 * other['pr'])
    sackRate = int(67 * other['pr'])
    defensiveChoices = []
    for player in other['players']:
        for x in range(round((player['ovr'] - 50) * player['passrush'])):
            defensiveChoices.append(player['name'])

    if rand <= pressureRate:
        didPressure = True
        rusher = choice(defensiveChoices)
    else:
        didPressure = False

    if rand <= sackRate:
        sackYards = int(6.5 * uniform(0.1, 1.9))
        return [True, didPressure, sackYards, rusher]
    else:
        return [False, didPressure]

def passPlay(team, other, pres, players, down, dist, length): # 64.8% average pass completion 2.4% average int rate using 45% pressure comp pct and 4% pressure int rate 13% deflect rate
    overall = team['players'][team['qb']]['ovr']
    baseDot = 8 # 7.88 average depth of target
    baseDot -= (2 - dist)
    dotGroups = [[0, 10], [11, 20], [21, 30], [31, 40], [41, 60]] # 1-10, 11-20, 21-30, 31-40, 40+
    maxInt = 1000
    if length < 41:
        maxInt -= 11
    if length < 31:
        maxInt -= 43
    if length < 21:
        maxInt -= 58
    if length < 11:
        maxInt -= 238
    dotGroup = randint(1, maxInt)
    if dotGroup <= 650:
        dotGroup = 0
    elif dotGroup <= 650 + 238:
        dotGroup = 1
    elif dotGroup <= 650 + 238 + 58:
        dotGroup = 2
    elif dotGroup <= 650 + 238 + 58 + 43:
        dotGroup = 3
    else:
        dotGroup = 4
    dotRange = dotGroups[dotGroup]
    if dotRange[1] > length:
        dotRange = [dotRange[0], length]
    dot = randint(dotRange[0], dotRange[1])
    # choices = []
    # k = 1
    # for y in range(baseDot + 1):
    #     for t in range(k):
    #         choices.append(y)
    #     k += 1
    # maxDist = length if length < 60 else 60
    # for y in range(baseDot + 1, maxDist):
    #     k -= 3
    #     for t in range(k):
    #         choices.append(y)
    # for y in range(0, length):
    #     for t in range(0, round(20*math.pow(math.e, -1 * (math.pow(y - baseDot, 2) / length*10)))):
    #         choices.append(y)
    # print(choices)

    # add = abs(choices[len(choices)])
    # print(choices)
    # dot = choice(choices)
    pcts = [784, 770, 756, 741, 727, 713, 699, 684, 670, 656, 641, 627, 613, 599, 584, 570, 556, 541, 527, 513, 499, 484, 470, 456, 441, 427, 413, 399, 384, 370, 356, 361, 352, 343, 334, 325, 315, 306, 297, 288, 279, 270, 365, 360, 355, 350, 345, 340, 335, 330, 325, 320, 315, 310, 305, 300, 295, 290, 285, 280, 275, 270]
    pct = pcts[dot]
    if pres:
        pct -= 10
    # basePct = 450 if pres else 648
    # yardRand = randint(round(-50*math.pi), 286)
    # yardFunction = round(10*math.tan(0.001*yardRand) + dist)
    receiverChoices = []
    recTotal = 0
    for player in team['players']:
        recTotal += player['target']
        for x in range(player['target']):
            receiverChoices.append(player['name'])
    for x in range(100 - recTotal):
            receiverChoices.append(team['name'] + ' WR')
    receiver = choice(receiverChoices)
    defenderChoices = []
    for player in team['players']:
        for x in range(round((player['ovr'] - 50) * player['coverage'])):
            defenderChoices.append(player['name'])
    defender = choice(defenderChoices)
    passPct = int((pct * ((((overall) / 85) + ((overall) / 85) + 1) / 3)) / other['pd'])
    rand = randint(1, 1000)
    if rand <= passPct:
        yac = randint(0, 10)
        return [True, False, False, False, dot + yac, receiver] # complete, deflect, int, reg incomplete, yards, receiver
    intPct = 30 if pres else 18
    intPct = int((intPct * ((((overall) / 85) + ((overall) / 85) + 1) / 3)) / other['pd'])
    if rand > (1000 - intPct):
        return [False, False, True, False, defender] # complete, deflect, int, reg incomplete, defender
    defPct = 130
    defPct = int((defPct * ((((overall) / 85) + ((overall) / 85) + 1) / 3)) / other['pd'])
    if rand > (1000 - intPct - defPct) and rand <= (1000 - intPct):
        return [False, True, False, False, defender] # complete, deflect, int, reg incomplete, defender
    
    return [False, False, False, True]

def runPlay(team, other, players, dist, length):
    # choices = [-2, -1, 0, 0]
    # k = 1
    # for y in range(round(distance / 2) + 1):
    #     for t in range(k):
    #         choices.append(y)
    #     k += 1
    # maxDist = length if length < 60 else 60
    # for y in range(round(distance / 2) + 1, length):
    #     if k > 1:
    #         k -= 2
    #     for t in range(k):
    #         choices.append(y)
    # return choice(choices)
    overall = team['players'][team['qb']]['ovr']
    runnerChoices = []
    for player in team['players']:
        for x in range(int(player['run'])):
            runnerChoices.append(player)
    runner = choice(runnerChoices)
    pctAdj = dist * 30
    pct = int((88 * ((((overall) / 85) + ((overall) / 85) + 1) / 3)) / other['rd']) * 10
    # pct = 880
    nextYard = True
    yards = 0
    while (nextYard):
        if randint(0, 1000) <= (pct + pctAdj):
            yards += 1
            pct -= int((30 * ((((overall) / 85) + ((overall) / 85) + 1) / 3)) / other['rd'])
        else:
            nextYard = False
            if yards == 0:
                yards -= randint(0, 3)
            return [yards, runner['name']]

    # mult = 0.01 + (dist / 100)
    # mult /= other['rd']
    # interval = round((math.log(length + 1))/(mult*math.log(2)))
    # rand = randint(0, interval)
    # rushYards = round(randRushYards(rand, mult))
    # return rushYards

def randRushYards(x, mult):
    return math.pow(2, mult*x) - 1

def randYards(center, mult, run, length, distance):
    if run:
        choices = []
        for x in range(2):
            choices.append(x)

    # 80 79 78 77 76 75 74 73

def fg(teamInd, team, long, score):
    mult = team['kmult']
    kickPcts = [1000, 990, 960, 950, 910, 860, 820, 720, 690, 410, 200] # 18-21, 22-25, 26-29, 30-33, 34-37, 38-41, 42-45, 46-49, 50-53, 54-57, 58-61, 62-65
    kickYds = [[18, 21], [22, 25], [26, 29], [30, 33], [34, 37], [38, 41], [42, 45], [46, 49], [50, 53], [54, 57], [58, 61], [62, 65]]
    for x in range(len(kickYds)):
        if long >= kickYds[x][0] and long <= kickYds[x][1]:
            pct = kickPcts[x]
            break
    pct = round(pct * mult)
    k = f"{team['name']} Kicker" if team['k'] < 0 else team['players'][team['k']]['name']
    if randint(0, 1000) > pct:
        score[teamInd] += 3
        print(f"{k} {long} yard field goal is good ({score[0]}-{score[1]})")
        playerStats[teamInd][k] = playerStats[teamInd].get(k, {})
        playerStats[teamInd][k]['ints'] = playerStats[teamInd][k].get('fgattempts', 0) + 1
        playerStats[teamInd][k] = playerStats[teamInd].get(k, {})
        playerStats[teamInd][k]['ints'] = playerStats[teamInd][k].get('fgmade', 0) + 1
        return True
    else:
        print(f"{k} {long} yard field goal is no good")
        playerStats[teamInd][k] = playerStats[teamInd].get(k, {})
        playerStats[teamInd][k]['ints'] = playerStats[teamInd][k].get('fgattempts', 0) + 1
        return False

def punt(teamInd, long):
    mult = teams[teamInd]['pmult']
    length = randint(35, 65)
    length *= mult
    if length > long:
        return [True]
    else:
        return [False, length]

def game():
    clock = 1800
    gameOver = False
    secondHalf = False
    down = 1
    dist = 10
    length = 80
    team = team1
    teamInd = 0
    score = [0, 0]
    last = ''
    while gameOver == False:
        while down < 4:
            result = play(team, teamInd, down, dist, length, last, score)
            last = result[2]
            clock -= 28
            if result[0] == False:
                down += 1
                dist -= result[1]
                length -= result[1]
                if dist <= 0:
                    if length >= 10:
                        dist = 10
                    else:
                        dist = length
                    down = 1
                if length <= 0:
                    score[teamInd] += 7
                    # print(f'Touchdown! The score is {score[0]}-{score[1]}')
                    down = 1
                    dist = 10
                    length = 80
                    if teamInd == 0:
                        teamInd = 1
                    else:
                        teamInd = 0
                    team = teams[teamInd]                   
                    stats['totalPoss'] += 1
                # else:
                    # print(f'It is now {down} and {dist} with {length} yards remaining!')
            else:
                print('Turnover!')
                down = 1
                length = 100 - length
                dist = length if length < 10 else 10
                if teamInd == 0:
                    teamInd = 1
                else:
                    teamInd = 0
                team = teams[teamInd]     
                stats['totalPoss'] += 1
            if clock <= 0:
                if secondHalf == True:
                    gameOver = True
                    break
                else:
                    secondHalf = True
                print(f'Halftime! The score is {score[0]}-{score[1]}')
                down = 1
                dist = 10
                length = 80
                teamInd = 1
                team = teams[teamInd]              
                clock = 1800
        if down == 4:
            if length + 17 <= team['kmax']:
                kick = fg(teamInd, team, length + 17, score)
                if kick:
                    score[teamInd] += 3
                    print(f'{length + 17} yard kick is good! The score is {score[0]}-{score[1]}')
                    down = 1
                    dist = 10
                    length = 80
                    if teamInd == 0:
                        teamInd = 1
                    else:
                        teamInd = 0
                    team = teams[teamInd]                    
                    stats['totalPoss'] += 1
                else:
                    print(f'{length + 17} yard kick is missed! The score is {score[0]}-{score[1]}')
                    down = 1
                    dist = 10
                    length = 100 - length
                    if teamInd == 0:
                        teamInd = 1
                    else:
                        teamInd = 0
                    team = teams[teamInd]                    
                    stats['totalPoss'] += 1
            else:
                puntResult = punt(teamInd, length + 14)
                if puntResult[0]:
                    print(f'The punt is a touchback! The score is {score[0]}-{score[1]}')
                    down = 1
                    dist = 10
                    length = 80
                    if teamInd == 0:
                        teamInd = 1
                    else:
                        teamInd = 0
                    team = teams[teamInd]                    
                    stats['totalPoss'] += 1
                else:
                    if randint(1, 1000) < 3:
                        if teamInd == 0:
                            teamInd = 1
                        else:
                            teamInd = 0
                        score[teamInd] += 7
                        if teamInd == 0:
                            teamInd = 1
                        else:
                            teamInd = 0
                        print(f'The punt is returned for a touchdown! The score is {score[0]}-{score[1]}')
                        down = 1
                        dist = 10
                        length = 100 - randint(18, 32)
                    else:
                        print(f'{puntResult[1]} yard punt! The score is {score[0]}-{score[1]}')
                        down = 1
                        dist = 10
                        length = 100 - (length + 14 - puntResult[1])
                        if teamInd == 0:
                            teamInd = 1
                        else:
                            teamInd = 0
                        team = teams[teamInd]
                        stats['totalPoss'] += 1
    
    print(f'Game over! Final score is {score[0]}-{score[1]}')
    print(stats)
    pp.pprint(playerStats[0])
    pp.pprint(playerStats[1])

game()
while input('Type Y and then hit enter to simulate the same game again') == 'Y':
    game()

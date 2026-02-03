import numpy as np
import random
top_8_points = []
top_1_points = []


MANCITY = 2342
INTER = 2291
LIVER = 2320
ARSENAL = 2250
REAL_MADRID = 2296
BARCELONA = 2285
BAYERN = 2223
ATLANTA = 2198
PSG = 2200
LEVRKUSEN = 2221
SPORTING = 2222
JUVENTUS = 2139
MILAN = 2107
DORTMUND = 2158
SPORTING = 2222
MONACO = 2096
BREST = 2010
ASTON_VILLA = 2078
LOSC = 2105
CELTIC = 2049
DINAMO = 1577
BENFICA = 2087
FEYENOORD = 2048
CLUB_BRUGGE = 1705
PSV = 2136
SPARTA_PRAHA = 2014
STUTTGART = 2108
SHAKHTAR = 1600
GIRONA = 2023
SALZBURG = 1598
BOLOGNA = 1759
LEIPZIG = 2130
STURM_GRAZ = 1574
YOUNG_BOYS = 1512
CRVENA_ZVEZDA = 1556
SLOVAN = 1418
ATLETICO_MADRID = 2138

points = {
    "MANCITY": 0, "INTER": 0, "LIVER": 0, "ARSENAL": 0, "REAL_MADRID": 0,
    "BARCELONA": 0, "BAYERN": 0, "ATLANTA": 0, "PSG": 0, "LEVRKUSEN": 0,
    "SPORTING": 0, "JUVENTUS": 0, "MILAN": 0, "DORTMUND": 0, "MONACO": 0,
    "BREST": 0, "ASTON_VILLA": 0, "LOSC": 0, "CELTIC": 0, "DINAMO": 0,
    "BENFICA": 0, "FEYENOORD": 0, "CLUB_BRUGGE": 0, "PSV": 0, "SPARTA_PRAHA": 0,
    "STUTTGART": 0, "SHAKHTAR": 0, "GIRONA": 0, "SALZBURG": 0, "BOLOGNA": 0,
    "LEIPZIG": 0, "STURM_GRAZ": 0, "YOUNG_BOYS": 0, "CRVENA_ZVEZDA": 0,
    "SLOVAN": 0, "ATLETICO_MADRID": 0
}


def ex_res(home_team, away_team, home_team_name, away_team_name):
    expected_resault = 1/(pow(10, -(home_team+100 - away_team)/400) + 1)

    if expected_resault + (15 * (expected_resault/100)) > random.random() > expected_resault - (15 * (expected_resault/100)):
        points[away_team_name] += 1
        points[home_team_name] += 1
    elif random.random() > expected_resault:
        points[away_team_name] += 3
    else:
        points[home_team_name] += 3


def matches():
    ex_res(BREST, STURM_GRAZ, "BREST", "STURM_GRAZ")
    ex_res(MONACO, BARCELONA, "MONACO", "BARCELONA")
    ex_res(ATLANTA, ARSENAL, "ATLANTA", "ARSENAL")
    ex_res(ATLETICO_MADRID, LEIPZIG, "ATLETICO_MADRID", "LEIPZIG")
    ex_res(FEYENOORD, LEVRKUSEN, "FEYENOORD", "LEVRKUSEN")
    ex_res(CRVENA_ZVEZDA, BENFICA, "CRVENA_ZVEZDA", "BENFICA")
    ex_res(CELTIC, SLOVAN, "CELTIC", "SLOVAN")
    ex_res(CLUB_BRUGGE, DORTMUND, "CLUB_BRUGGE", "DORTMUND")
    ex_res(PSG, GIRONA, "PSG", "GIRONA")
    ex_res(MANCITY, INTER, "MANCITY", "INTER")
    ex_res(BOLOGNA, SHAKHTAR, "BOLOGNA", "SHAKHTAR")
    ex_res(SPARTA_PRAHA, SALZBURG, "SPARTA_PRAHA", "SALZBURG")
    ex_res(REAL_MADRID, STUTTGART, "REAL_MADRID", "STUTTGART")
    ex_res(SPORTING, LOSC, "SPORTING", "LOSC")
    ex_res(BAYERN, DINAMO, "BAYERN", "DINAMO")
    ex_res(MILAN, LIVER, "MILAN", "LIVER")
    ex_res(JUVENTUS, PSV, "JUVENTUS", "PSV")
    ex_res(YOUNG_BOYS, ASTON_VILLA, "YOUNG_BOYS", "ASTON_VILLA")
    ex_res(SALZBURG, BREST, "SALZBURG", "BREST")
    ex_res(STUTTGART, SPARTA_PRAHA, "STUTTGART", "SPARTA_PRAHA")
    ex_res(ASTON_VILLA, BAYERN, "ASTON_VILLA", "BAYERN")
    ex_res(LEIPZIG, JUVENTUS, "LEIPZIG", "JUVENTUS")
    ex_res(LIVER, BOLOGNA, "LIVER", "BOLOGNA")
    ex_res(BENFICA, ATLETICO_MADRID, "BENFICA", "ATLETICO_MADRID")
    ex_res(STURM_GRAZ, CLUB_BRUGGE, "STURM_GRAZ", "CLUB_BRUGGE")
    ex_res(DINAMO, MONACO, "DINAMO", "MONACO")
    ex_res(LOSC, REAL_MADRID, "LOSC", "REAL_MADRID")
    ex_res(SHAKHTAR, ATLANTA, "SHAKHTAR", "ATLANTA")
    ex_res(GIRONA, FEYENOORD, "GIRONA", "FEYENOORD")
    ex_res(INTER, CRVENA_ZVEZDA, "INTER", "CRVENA_ZVEZDA")
    ex_res(BARCELONA, YOUNG_BOYS, "BARCELONA", "YOUNG_BOYS")
    ex_res(LEVRKUSEN, MILAN, "LEVRKUSEN", "MILAN")
    ex_res(DORTMUND, CELTIC, "DORTMUND", "CELTIC")
    ex_res(PSV, SPORTING, "PSV", "SPORTING")
    ex_res(SLOVAN, MANCITY, "SLOVAN", "MANCITY")
    ex_res(ARSENAL, PSG, "ARSENAL", "PSG")
    ex_res(LEIPZIG, LIVER, "LEIPZIG", "LIVER")
    ex_res(MANCITY, SPARTA_PRAHA, "MANCITY", "SPARTA_PRAHA")
    ex_res(BENFICA, FEYENOORD, "BENFICA", "FEYENOORD")
    ex_res(ATLETICO_MADRID, LOSC, "ATLETICO_MADRID", "LOSC")
    ex_res(BARCELONA, BAYERN, "BARCELONA", "BAYERN")
    ex_res(YOUNG_BOYS, INTER, "YOUNG_BOYS", "INTER")
    ex_res(SALZBURG, DINAMO, "SALZBURG", "DINAMO")
    ex_res(BREST, LEVRKUSEN, "BREST", "LEVRKUSEN")
    ex_res(ATLANTA, CELTIC, "ATLANTA", "CELTIC")
    ex_res(ARSENAL, SHAKHTAR, "ARSENAL", "SHAKHTAR")
    ex_res(JUVENTUS, STUTTGART, "JUVENTUS", "STUTTGART")
    ex_res(PSG, PSV, "PSG", "PSV")
    ex_res(ASTON_VILLA, BOLOGNA, "ASTON_VILLA", "BOLOGNA")
    ex_res(GIRONA, SLOVAN, "GIRONA", "SLOVAN")
    ex_res(REAL_MADRID, DORTMUND, "REAL_MADRID", "DORTMUND")
    ex_res(STURM_GRAZ, SPORTING, "STURM_GRAZ", "SPORTING")
    ex_res(MONACO, CRVENA_ZVEZDA, "MONACO", "CRVENA_ZVEZDA")
    ex_res(MILAN, CLUB_BRUGGE, "MILAN", "CLUB_BRUGGE")
    ex_res(SLOVAN, DINAMO, "SLOVAN", "DINAMO")
    ex_res(PSV, GIRONA, "PSV", "GIRONA")
    ex_res(REAL_MADRID, MILAN, "REAL_MADRID", "MILAN")
    ex_res(SPORTING, MANCITY, "SPORTING", "MANCITY")
    ex_res(LIVER, LEVRKUSEN, "LIVER", "LEVRKUSEN")
    ex_res(CELTIC, LEIPZIG, "CELTIC", "LEIPZIG")
    ex_res(BOLOGNA, MONACO, "BOLOGNA", "MONACO")
    ex_res(DORTMUND, STURM_GRAZ, "DORTMUND", "STURM_GRAZ")
    ex_res(LOSC, JUVENTUS, "LOSC", "JUVENTUS")
    ex_res(CLUB_BRUGGE, ASTON_VILLA, "CLUB_BRUGGE", "ASTON_VILLA")
    ex_res(SHAKHTAR, YOUNG_BOYS, "SHAKHTAR", "YOUNG_BOYS")
    ex_res(PSG, ATLETICO_MADRID, "PSG", "ATLETICO_MADRID")
    ex_res(FEYENOORD, SALZBURG, "FEYENOORD", "SALZBURG")
    ex_res(INTER, ARSENAL, "INTER", "ARSENAL")
    ex_res(BAYERN, BENFICA, "BAYERN", "BENFICA")
    ex_res(CRVENA_ZVEZDA, BARCELONA, "CRVENA_ZVEZDA", "BARCELONA")
    ex_res(STUTTGART, ATLANTA, "STUTTGART", "ATLANTA")
    ex_res(SPARTA_PRAHA, BREST, "SPARTA_PRAHA", "BREST")
    ex_res(SPARTA_PRAHA, ATLETICO_MADRID, "SPARTA_PRAHA", "ATLETICO_MADRID")
    ex_res(SLOVAN, MILAN, "SLOVAN", "MILAN")
    ex_res(YOUNG_BOYS, ATLANTA, "YOUNG_BOYS", "ATLANTA")
    ex_res(BAYERN, PSG, "BAYERN", "PSG")
    ex_res(BARCELONA, BREST, "BARCELONA", "BREST")
    ex_res(LEVRKUSEN, SALZBURG, "LEVRKUSEN", "SALZBURG")
    ex_res(INTER, LEIPZIG, "INTER", "LEIPZIG")
    ex_res(MANCITY, FEYENOORD, "MANCITY", "FEYENOORD")
    ex_res(SPORTING, ARSENAL, "SPORTING", "ARSENAL")
    ex_res(STURM_GRAZ, GIRONA, "STURM_GRAZ", "GIRONA")
    ex_res(CRVENA_ZVEZDA, STUTTGART, "CRVENA_ZVEZDA", "STUTTGART")
    ex_res(DINAMO, DORTMUND, "DINAMO", "DORTMUND")
    ex_res(MONACO, BENFICA, "MONACO", "BENFICA")
    ex_res(PSV, SHAKHTAR, "PSV", "SHAKHTAR")
    ex_res(LIVER, REAL_MADRID, "LIVER", "REAL_MADRID")
    ex_res(BOLOGNA, LOSC, "BOLOGNA", "LOSC")
    ex_res(CELTIC, CLUB_BRUGGE, "CELTIC", "CLUB_BRUGGE")
    ex_res(ASTON_VILLA, JUVENTUS, "ASTON_VILLA", "JUVENTUS")
    ex_res(GIRONA, LIVER, "GIRONA", "LIVER")
    ex_res(DINAMO, CELTIC, "DINAMO", "CELTIC")
    ex_res(SALZBURG, PSG, "SALZBURG", "PSG")
    ex_res(BREST, PSV, "BREST", "PSV")
    ex_res(CLUB_BRUGGE, SPORTING, "CLUB_BRUGGE", "SPORTING")
    ex_res(ATLANTA, REAL_MADRID, "ATLANTA", "REAL_MADRID")
    ex_res(LEVRKUSEN, INTER, "INTER", "LEVRKUSEN")
    ex_res(SHAKHTAR, BAYERN, "SHAKHTAR", "BAYERN")
    ex_res(LEIPZIG, ASTON_VILLA, "LEIPZIG", "ASTON_VILLA")
    ex_res(ATLETICO_MADRID, SLOVAN, "ATLETICO_MADRID", "SLOVAN")
    ex_res(LOSC, STURM_GRAZ, "LOSC", "STURM_GRAZ")
    ex_res(STUTTGART, YOUNG_BOYS, "STUTTGART", "YOUNG_BOYS")
    ex_res(ARSENAL, MONACO, "ARSENAL", "MONACO")
    ex_res(MILAN, CRVENA_ZVEZDA, "MILAN", "CRVENA_ZVEZDA")
    ex_res(BENFICA, BOLOGNA, "BENFICA", "BOLOGNA")
    ex_res(DORTMUND, BARCELONA, "DORTMUND", "BARCELONA")
    ex_res(FEYENOORD, SPARTA_PRAHA, "FEYENOORD", "SPARTA_PRAHA")
    ex_res(JUVENTUS, MANCITY, "JUVENTUS", "MANCITY")
    ex_res(ATLANTA, STURM_GRAZ, "ATLANTA", "STURM_GRAZ")
    ex_res(MONACO, ASTON_VILLA, "MONACO", "ASTON_VILLA")
    ex_res(LIVER, LOSC, "LIVER", "LOSC")
    ex_res(BOLOGNA, DORTMUND, "BOLOGNA", "DORTMUND")
    ex_res(BENFICA, BARCELONA, "BENFICA", "BARCELONA")
    ex_res(ATLETICO_MADRID, LEVRKUSEN, "ATLETICO_MADRID", "LEVRKUSEN")
    ex_res(CLUB_BRUGGE, JUVENTUS, "CLUB_BRUGGE", "JUVENTUS")
    ex_res(CRVENA_ZVEZDA, PSV, "CRVENA_ZVEZDA", "PSV")
    ex_res(SLOVAN, STUTTGART, "SLOVAN", "STUTTGART")
    ex_res(LEIPZIG, SPORTING, "LEIPZIG", "SPORTING")
    ex_res(SHAKHTAR, BREST, "SHAKHTAR", "BREST")
    ex_res(REAL_MADRID, SALZBURG, "REAL_MADRID", "SALZBURG")
    ex_res(PSG, MANCITY, "PSG", "MANCITY")
    ex_res(CELTIC, YOUNG_BOYS, "CELTIC", "YOUNG_BOYS")
    ex_res(FEYENOORD, BAYERN, "FEYENOORD", "BAYERN")
    ex_res(MILAN, GIRONA, "MILAN", "GIRONA")
    ex_res(ARSENAL, DINAMO, "ARSENAL", "DINAMO")
    ex_res(SPARTA_PRAHA, INTER, "SPARTA_PRAHA", "INTER")
    ex_res(ASTON_VILLA, CELTIC, "ASTON_VILLA", "CELTIC")
    ex_res(BARCELONA, ATLANTA, "BARCELONA", "ATLANTA")
    ex_res(LEVRKUSEN, SPARTA_PRAHA, "LEVRKUSEN", "SPARTA_PRAHA")
    ex_res(BAYERN, SLOVAN, "BAYERN", "SLOVAN")
    ex_res(DORTMUND, SHAKHTAR, "DORTMUND", "SHAKHTAR")
    ex_res(GIRONA, ARSENAL, "GIRONA", "ARSENAL")
    ex_res(INTER, MONACO, "INTER", "MONACO")
    ex_res(BREST, REAL_MADRID, "BREST", "REAL_MADRID")
    ex_res(SALZBURG, ATLETICO_MADRID, "SALZBURG", "ATLETICO_MADRID")
    ex_res(YOUNG_BOYS, CRVENA_ZVEZDA, "YOUNG_BOYS", "CRVENA_ZVEZDA")
    ex_res(STUTTGART, PSG, "STUTTGART", "PSG")
    ex_res(LOSC, FEYENOORD, "LOSC", "FEYENOORD")
    ex_res(DINAMO, MILAN, "DINAMO", "MILAN")
    ex_res(PSV, LIVER, "PSV", "LIVER")
    ex_res(MANCITY, CLUB_BRUGGE, "MANCITY", "CLUB_BRUGGE")
    ex_res(JUVENTUS, BENFICA, "JUVENTUS", "BENFICA")
    ex_res(SPORTING, BOLOGNA, "SPORTING", "BOLOGNA")
    ex_res(STURM_GRAZ, LEIPZIG, "STURM_GRAZ", "LEIPZIG")


for _ in range(10000):
    matches()


def sorting():
    sorted_teams = sorted(points.items(), key=lambda x: x[1], reverse=True)
    return sorted_teams


sorted_teams = sorting()


print(f"{'Rank':<5}{'Team':<20}{'Points'}")
print("----------------------")


for rank, (team, point) in enumerate(sorted_teams, start=1):
    print(f"{rank:<5}{team:<20}{point / 10000:.3f}")

for _ in range(10000):
    top_8_points.append(sorted_teams[7][1]/10000)
for _ in range(10000):
    top_1_points.append(sorted_teams[0][1]/10000)


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


average_points_for_top_8 = calculate_average(top_8_points)
average_points_for_top_1 = calculate_average(top_1_points)
print(f"Average points needed to stay in the top 8: {
      average_points_for_top_8:.2f}")


min_points_for_top_8 = float('inf')

points_of_9th_place = sorted_teams[8][1]

min_points_for_top_8 = min(min_points_for_top_8, points_of_9th_place + 1)
min_points_for_top_8 = min_points_for_top_8/1000
print(f"Minimum points needed to secure a top 8 spot: {
      min_points_for_top_8:.2f}")
print(f"Average points needed to be in the top 1: {
      average_points_for_top_1:.2f}")

import pandas as pd

# Define a dictionary with MLB player statistics
data = {
    "PlayerID": list(range(1, 21)),
    "PlayerName": [
        "Mike Trout", "Mookie Betts", "Bryce Harper", "Aaron Judge", "Shohei Ohtani",
        "Juan Soto", "Freddie Freeman", "Vladimir Guerrero Jr.", "Tatis Jr.", "Ronald Acuña Jr.",
        "Jose Ramirez", "Buster Posey", "Carlos Correa", "Xander Bogaerts", "Giancarlo Stanton",
        "Nolan Arenado", "George Springer", "Luis Robert", "Ketel Marte", "Jack Flaherty"
    ],
    "Team": [
        "Angels", "Dodgers", "Phillies", "Yankees", "Angels",
        "Nationals", "Braves", "Blue Jays", "Padres", "Braves",
        "Indians", "Giants", "Astros", "Red Sox", "Yankees",
        "Cardinals", "Blue Jays", "White Sox", "Diamondbacks", "Cardinals"
    ],
    "Position": [
        "CF", "RF", "RF", "RF", "DH",
        "RF", "1B", "1B", "SS", "RF",
        "3B", "C", "SS", "SS", "DH",
        "3B", "CF", "CF", "2B", "SP"
    ],
    "GamesPlayed": [
        140, 142, 137, 148, 130,
        143, 155, 158, 143, 147,
        142, 138, 150, 156, 145,
        150, 140, 135, 140, 25
    ],
    "HomeRuns": [
        45, 32, 35, 40, 35,
        29, 31, 36, 42, 41,
        38, 24, 23, 25, 27,
        34, 30, 32, 29, 8
    ],
    "BattingAverage": [
        0.305, 0.291, 0.282, 0.287, 0.276,
        0.320, 0.307, 0.308, 0.286, 0.290,
        0.270, 0.304, 0.277, 0.300, 0.239,
        0.289, 0.259, 0.262, 0.318, 0.241
    ],
    "RBIs": [
        104, 80, 98, 102, 88,
        95, 99, 112, 101, 90,
        89, 60, 64, 75, 67,
        102, 76, 65, 77, 20
    ]
}
# Create a DataFrame from the dictionary
df_mlb_stats = pd.DataFrame(data)

# Print the DataFrame
print(df_mlb_stats)


groups = df_mlb_stats.groupby("Team")

for name,group in groups:
    print(f"\nTeam Name:{name}\n")
    print(f"{group}\n")
    
    
print(f"\n\n\n\n{groups.get_group('Angels')}\n") # Gets the group with team name angels

u18_team = groups.filter(lambda x : x['HomeRuns'].sum() > 40 )
print(f"{u18_team}\n")


# We can also pass multiple element for grouping such as

groups2 = df_mlb_stats.groupby(["Position","Team"])

for name,group in groups:
    print(f"{name}\n\n")
    print(f"{group}\n\n")
    
    


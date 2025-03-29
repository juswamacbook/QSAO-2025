import pandas as pd

def extract_atl_players(file_path):
    # Load the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Load data from the first sheet
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    
    # Filter players from team 'ATL'
    atl_players = df[df["Team"] == "ATL"]
    
    # Convert to list of dictionaries
    return atl_players.to_dict(orient="records")

# Example usage
file_path = "QSAO CASECOMP PLAYERDATA.xlsx"  # Update with your file path
players_list = extract_atl_players(file_path)


players_by_position = {}
for player in players_list:
    pos = player["Pos"]
    if pos not in players_by_position:
        players_by_position[pos] = []
    players_by_position[pos].append(player)
    
    # Sort players by age (youngest to oldest
players_by_age = sorted(players_list, key=lambda x: x["Age"])

# print all atl players
#for player in players_list:
    #print(player)

# print list of positions
#for player in players_by_position:
    #print(player)

# print list by age
for player in players_by_age:
    print(player)

print (len(players_list))
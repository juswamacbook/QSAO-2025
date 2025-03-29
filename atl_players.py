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
atl_players_list = extract_atl_players(file_path)

# Print sample output
for player in atl_players_list:
    print(player)

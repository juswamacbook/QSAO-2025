import pandas as pd
import matplotlib.pyplot as plt

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

# Calculate DRB per 36 minutes for each player
for player in players_list:
    drb = player.get("DRB", 0)
    mp = player.get("MP", 0)
    
    # Avoid division by zero
    if mp > 0:
        # Calculate DRB per 36 minutes
        player["DRB_per_36"] = (drb / mp) * 36
    else:
        player["DRB_per_36"] = 0

# Sort players by DRB per 36 minutes
players_by_drb_per_36 = sorted(players_list, key=lambda x: x.get("DRB_per_36", 0), reverse=True)

# Create lists for player names and their DRB per 36 values
player_names = [player['Player'] for player in players_by_drb_per_36]
drb_per_36_values = [player.get('DRB_per_36', 0) for player in players_by_drb_per_36]

# Create the bar chart
plt.figure(figsize=(12, 8))  # Adjust figure size as needed
bars = plt.bar(player_names, drb_per_36_values)

# Add title and labels
plt.title('Atlanta Hawks Players: Defensive Rebounds per 36 Minutes', fontsize=16)
plt.xlabel('Players', fontsize=14)
plt.ylabel('DRB per 36 Minutes', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=10)

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{height:.2f}', ha='center', va='bottom', fontsize=9)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.savefig('atl_players_drb_per_36.png')  # Save the figure
plt.show()  # Display the figure

print("Bar chart created and saved as 'atl_players_drb_per_36.png'")
import pandas as pd
import random
import numpy as np

from team import Team
from group_match_simulator import GroupMatchSimulator

class Group:
    def __init__(self, team_names):
        self.team_names = team_names
        self.table = self.create_dataframe()

    def create_dataframe(self):
        # Extract Teams objects based on team_names
        teams_data = [Team.teams_info_dict[name] for name in self.team_names if name in Team.teams_info_dict]
        
        # Create a DataFrame
        df = pd.DataFrame(data=[(team.name, team.elo, 0) for team in teams_data], columns=['TEAM', 'ELO', 'POINTS'], index=range(1, len(teams_data) + 1))
        return df
    
    def create_match_list(self):
        # Get the team names and ELO from the dataframe
        team_names = self.table['TEAM'].tolist()
        team_elo = self.table['ELO'].tolist()
        
        # Create a list of matches with ELO
        match_list = []
        for i in range(len(team_names) // 2):
            match_list.append(((team_names[i], team_elo[i]), (team_names[-(i+1)], team_elo[-(i+1)])))
        
        # Add remaining tuples
        match_list.append(((team_names[0], team_elo[0]), (team_names[1], team_elo[1])))
        match_list.append(((team_names[2], team_elo[2]), (team_names[3], team_elo[3])))
        match_list.append(((team_names[0], team_elo[0]), (team_names[2], team_elo[2])))
        match_list.append(((team_names[1], team_elo[1]), (team_names[3], team_elo[3])))
        
        return match_list
    
    def get_final_standings(self):
        # Sort by POINTS descending, then by ELO descending as a preliminary step
        sorted_df = self.table.sort_values(by=['POINTS', 'ELO'], ascending=[False, False])
        
        # Reset index to iterate over DataFrame rows, without dropping the old index
        sorted_df.reset_index(drop=True, inplace=True)
        
        # Iterate over the DataFrame to handle ties
        i = 0
        while i < len(sorted_df) - 1:
            # If there's a tie on points
            if sorted_df.loc[i, 'POINTS'] == sorted_df.loc[i + 1, 'POINTS']:
                start = i
                # Find the range of the tie
                while i < len(sorted_df) - 1 and sorted_df.loc[i, 'POINTS'] == sorted_df.loc[i + 1, 'POINTS']:
                    i += 1
                end = i
                
                # For each pair in the tie, probabilistically decide who wins the tie based on Elo
                for j in range(start, end):
                    if np.random.rand() > 0.6:  # 40% chance to swap with the next team
                        # Swap rows
                        sorted_df.iloc[[j, j + 1]] = sorted_df.iloc[[j + 1, j]].values
            i += 1

        # Adjust the DataFrame index to start from 1
        sorted_df.index = range(1, len(sorted_df) + 1)
        
        self.final_standings = sorted_df
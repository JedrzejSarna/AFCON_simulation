import pandas as pd
import random
import numpy as np


class Team:
    teams_info_dict = {}

    def __init__(self, name, elo):
        self.name = name
        self.elo = elo
        Team.teams_info_dict[self.name] = self

    def get_name(self):
        return self.name

    def get_elo(self):
        return self.elo

    def set_elo(self, elo):
        self.elo = elo

    @classmethod
    def ELO_ranking_for_teams(cls):
        # Convert the dictionary to a list of dictionaries for DataFrame creation
        teams_list = [{'Name': team.name, 'ELO': team.elo} for team in cls.teams_info_dict.values()]
        df = pd.DataFrame(teams_list)
        # Sort the DataFrame by the 'Elo' column
        sorted_df = df.sort_values(by='ELO', ascending=False)
        # Reset the index starting from 1
        sorted_df.index = range(1, len(sorted_df) + 1)
        return sorted_df
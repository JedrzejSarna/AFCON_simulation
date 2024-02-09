import pandas as pd
import random
import numpy as np



class GroupMatchSimulator:
    def __init__(self, group_instance):
        self.group_instance = group_instance

    def calculate_win_probability(self, rating_a, rating_b):
        """
        Calculate the probability of winning for team_a.
        """
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    def simulate_match(self, team_a, team_b):
        """
        Simulate a match between team_a and team_b based on their Elo ratings
        and return the points as a tuple (points_team_a, points_team_b).
        """
        prob_a_wins = self.calculate_win_probability(team_a[1], team_b[1])
        prob_b_wins = self.calculate_win_probability(team_b[1], team_a[1])

        # Simulate the match based on probabilities
        random_chance = random.random()
        if random_chance < prob_a_wins:
            # Team A wins
            return (3, 0)
        elif random_chance < prob_a_wins + prob_b_wins:  # Adjust for draw probability
            # Team B wins
            return (0, 3)
        else:
            # Draw
            return (1, 1)

    def get_results(self): 
        results = [self.simulate_match(team_a, team_b) for team_a, team_b in self.group_instance.create_match_list()]
        return results
    
    def get_total_points(self):
        team_points = {}
        for team, result in zip(self.group_instance.create_match_list(), self.get_results()):
            team_a, team_b = team
            points_a, points_b = result

            # Update team A's points
            if team_a in team_points:
                team_points[team_a] += points_a
            else:
                team_points[team_a] = points_a

            # Update team B's points
            if team_b in team_points:
                team_points[team_b] += points_b
            else:
                team_points[team_b] = points_b

        return team_points
    
    def update_table(self):
        team_points = self.get_total_points()
        self.group_instance.table['POINTS'] = [team_points.get((team, elo), 0) for team, elo in zip(self.group_instance.table['TEAM'], self.group_instance.table['ELO'])]

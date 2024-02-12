import pandas as pd
import random

class KnockoutStage:
    def __init__(self, group_a, group_b, group_c, group_d, group_e, group_f, third_places):
        self.group_A = group_a
        self.group_B = group_b
        self.group_C = group_c
        self.group_D = group_d
        self.group_E = group_e
        self.group_F = group_f
        self.group_3rd = third_places

        winners_and_runners_up = [
            group_a.table.iloc[0:2],
            group_b.table.iloc[0:2],
            group_c.table.iloc[0:2],
            group_d.table.iloc[0:2],
            group_e.table.iloc[0:2],
            group_f.table.iloc[0:2],
        ]
        
        #taking the top 4 third-placed teams
        best_thirds = third_places.iloc[0:4]
        
        # Combine all qualified teams
        qualified_teams = pd.concat(winners_and_runners_up + [best_thirds]).reset_index(drop=True)
        qualified_teams['ELO'] = qualified_teams['ELO'] + qualified_teams['POINTS']*5
        self.qualified_teams = qualified_teams


        self.round16_matches = [
            # Runner-up Group A vs Runner-up Group C
            (self.qualified_teams.iloc[1], self.qualified_teams.iloc[5]),
            # Winner Group D vs Best 3rd place 4
            (self.qualified_teams.iloc[6], self.qualified_teams.iloc[15]),
            # Winner Group B vs Best 3rd place 2
            (self.qualified_teams.iloc[2], self.qualified_teams.iloc[13]),
            # Winner Group F vs Runner-up Group E
            (self.qualified_teams.iloc[10], self.qualified_teams.iloc[9]),
            # Runner-up Group B vs Runner-up Group F
            (self.qualified_teams.iloc[3], self.qualified_teams.iloc[11]),
            # Winner Group A vs Best 3rd place 1
            (self.qualified_teams.iloc[0], self.qualified_teams.iloc[12]),
            # Winner Group E vs Runner-up Group D
            (self.qualified_teams.iloc[8], self.qualified_teams.iloc[7]),
            # Winner Group C vs Best 3rd place 3
            (self.qualified_teams.iloc[4], self.qualified_teams.iloc[14]),
        ]

    def calculate_win_probability(self, rating_a, rating_b):
        """
        Calculate the probability of winning for team_a.
        """
        return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))





    def show_matches_and_probabilities_round_of_16(self):
        for match in self.round16_matches:
            prob_a_wins = round(self.calculate_win_probability(match[0].iloc[1], match[1].iloc[1]), 2)
            prob_b_wins = round(self.calculate_win_probability(match[1].iloc[1], match[0].iloc[1]) , 2)

            print(f"{match[0].iloc[0]} vs {match[1].iloc[0]} WIN A: {prob_a_wins} WIN B: {prob_b_wins}")

    def simulate_round_of_16(self):
        winning_indices = []  # Store indices of winning teams
        for match in self.round16_matches:
            prob_a_wins = self.calculate_win_probability(match[0]['ELO'], match[1]['ELO'])
            outcome = random.random()  # Generate a random float in the range [0.0, 1.0)
            if outcome < prob_a_wins:
                winning_indices.append(match[0].name) 
            else:
                winning_indices.append(match[1].name)

        # Filter self.qualified_teams to only include the winners
        self.round_of_16_winners = self.qualified_teams.loc[winning_indices].reset_index(drop=True)



        self.quarter_finals_matches = [
            (self.round_of_16_winners.iloc[0], self.round_of_16_winners.iloc[1]),
            (self.round_of_16_winners.iloc[2], self.round_of_16_winners.iloc[3]),
            (self.round_of_16_winners.iloc[4], self.round_of_16_winners.iloc[5]),
            (self.round_of_16_winners.iloc[6], self.round_of_16_winners.iloc[7])
        ]




    def show_matches_and_probabilities_quarter_finals(self):
        for match in self.quarter_finals_matches:
            prob_a_wins = round(self.calculate_win_probability(match[0].iloc[1], match[1].iloc[1]), 2)
            prob_b_wins = round(self.calculate_win_probability(match[1].iloc[1], match[0].iloc[1]) , 2)

            print(f"{match[0].iloc[0]} vs {match[1].iloc[0]} WIN A: {prob_a_wins} WIN B: {prob_b_wins}")

    def simulate_quarter_finals(self):
        winning_indices = [] 
        for match in self.quarter_finals_matches:
            prob_a_wins = self.calculate_win_probability(match[0]['ELO'], match[1]['ELO'])
            outcome = random.random() 
            if outcome < prob_a_wins:
                winning_indices.append(match[0].name) 
            else:
                winning_indices.append(match[1].name)

        self.quarter_finals_winners = self.round_of_16_winners.loc[winning_indices].reset_index(drop=True)

        self.semi_finals_matches = [
            (self.quarter_finals_winners.iloc[0], self.quarter_finals_winners.iloc[1]),
            (self.quarter_finals_winners.iloc[2], self.quarter_finals_winners.iloc[3])
        ]

    def show_matches_and_probabilities_semi_finals(self):
        for match in self.semi_finals_matches:
            prob_a_wins = round(self.calculate_win_probability(match[0].iloc[1], match[1].iloc[1]), 2)
            prob_b_wins = round(self.calculate_win_probability(match[1].iloc[1], match[0].iloc[1]) , 2)

            print(f"{match[0].iloc[0]} vs {match[1].iloc[0]} WIN A: {prob_a_wins} WIN B: {prob_b_wins}")

    def simulate_semi_finals(self):
        winning_indices = []
        for match in self.semi_finals_matches:
            prob_a_wins = self.calculate_win_probability(match[0]['ELO'], match[1]['ELO'])
            outcome = random.random()
            if outcome < prob_a_wins:
                winning_indices.append(match[0].name)  
            else:
                winning_indices.append(match[1].name)
        
        self.finalists = self.quarter_finals_winners.loc[winning_indices].reset_index(drop=True)
        self.semi_finals_losers = self.quarter_finals_winners.loc[~self.quarter_finals_winners.index.isin(winning_indices)].reset_index(drop=True)

        self.final_match = [
            (self.finalists.iloc[0], self.finalists.iloc[1])
        ]
        self.third_place_playoff = [
            (self.semi_finals_losers.iloc[0], self.semi_finals_losers.iloc[1])
        ]


    def show_match_and_probabilities_third_place_playoff(self):
        for match in self.third_place_playoff:
            prob_a_wins = round(self.calculate_win_probability(match[0].iloc[1], match[1].iloc[1]), 2)
            prob_b_wins = round(self.calculate_win_probability(match[1].iloc[1], match[0].iloc[1]) , 2)

            print(f"{match[0].iloc[0]} vs {match[1].iloc[0]} WIN A: {prob_a_wins} WIN B: {prob_b_wins}")

    def simulate_third_place_playoff(self):
        winning_indices = [] 
        for match in self.third_place_playoff:
            prob_a_wins = self.calculate_win_probability(match[0]['ELO'], match[1]['ELO'])
            outcome = random.random() 
            if outcome < prob_a_wins:
                winning_indices.append(match[0].name)  
            else:
                winning_indices.append(match[1].name)

        self.THIRD_PLACE = self.semi_finals_losers.loc[winning_indices].reset_index(drop=True)



    def show_match_and_probabilities_final(self):
        for match in self.final_match:
            prob_a_wins = round(self.calculate_win_probability(match[0].iloc[1], match[1].iloc[1]), 2)
            prob_b_wins = round(self.calculate_win_probability(match[1].iloc[1], match[0].iloc[1]) , 2)

            print(f"{match[0].iloc[0]} vs {match[1].iloc[0]} WIN A: {prob_a_wins} WIN B: {prob_b_wins}")

    def simulate_final(self):
        winning_indices = []  
        for match in self.final_match:
            prob_a_wins = self.calculate_win_probability(match[0]['ELO'], match[1]['ELO'])
            outcome = random.random()  
            if outcome < prob_a_wins:
                winning_indices.append(match[0].name)
            else:
                winning_indices.append(match[1].name)

        self.SECOND_PLACE = self.finalists.loc[~self.finalists.index.isin(winning_indices)].reset_index(drop=True)
        self.WINNER = self.finalists.loc[winning_indices].reset_index(drop=True)['TEAM'].item()
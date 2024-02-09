from team import *
from group import *
from group_match_simulator import *

import pandas as pd
import random
import numpy as np



team = {
    "Ivory_Coast": Team("Ivory_Coast", 1647),
    "Nigeria": Team("Nigeria", 1568),
    "Equatorial_Guinea": Team("Equatorial_Guinea", 1507),
    "Guinea-Bissau": Team("Guinea-Bissau", 1410),
    "Egypt": Team("Egypt", 1688),
    "Ghana": Team("Ghana", 1544),
    "Cape_Verde": Team("Cape_Verde", 1478),
    "Mozambique": Team("Mozambique", 1366),
    "Senegal": Team("Senegal", 1732),
    "Cameroon": Team("Cameroon", 1616),
    "Guinea": Team("Guinea", 1449),
    "Gambia": Team("Gambia", 1399),
    "Algeria": Team("Algeria", 1736),
    "Burkina_Faso": Team("Burkina_Faso", 1571),
    "Mauritania": Team("Mauritania", 1401),
    "Angola": Team("Angola", 1409),
    "Tunisia": Team("Tunisia", 1735),
    "Mali": Team("Mali", 1622),
    "South_Africa": Team("South_Africa", 1482),
    "Namibia": Team("Namibia", 1388),
    "Morocco": Team("Morocco", 1848),
    "Democratic_Republic_of_Congo": Team("Democratic_Republic_of_Congo", 1489),
    "Zambia": Team("Zambia", 1494),
    "Tanzania": Team("Tanzania", 1349)
}
Team.ELO_ranking_for_teams()

group_a_names = ["Ivory_Coast", "Nigeria", "Equatorial_Guinea", "Guinea-Bissau"]
group_b_names = ["Egypt", "Ghana", "Cape_Verde", "Mozambique"]
group_c_names = ["Senegal", "Cameroon", "Guinea", "Gambia"]
group_d_names = ["Algeria", "Burkina_Faso", "Mauritania", "Angola"]
group_e_names = ["Tunisia", "Mali", "South_Africa", "Namibia"]
group_f_names = ["Morocco", "Democratic_Republic_of_Congo", "Zambia", "Tanzania"]

group_A = Group(group_a_names)
group_B = Group(group_b_names)
group_C = Group(group_c_names)
group_D = Group(group_d_names)
group_E = Group(group_e_names)
group_F = Group(group_f_names)

group_A_matches = GroupMatchSimulator(group_A)
group_A_matches.update_table()
group_B_matches = GroupMatchSimulator(group_B)
group_B_matches.update_table()
group_C_matches = GroupMatchSimulator(group_C)
group_C_matches.update_table()
group_D_matches = GroupMatchSimulator(group_D)
group_D_matches.update_table()
group_E_matches = GroupMatchSimulator(group_E)
group_E_matches.update_table()
group_F_matches = GroupMatchSimulator(group_F)
group_F_matches.update_table()

group_A.table
group_B.table

group_A.get_final_standings()
group_B.get_final_standings()
group_C.get_final_standings()
group_D.get_final_standings()
group_E.get_final_standings()
group_F.get_final_standings()

group_A.final_standings
group_B.final_standings
group_C.final_standings
group_D.final_standings
group_E.final_standings
group_F.final_standings
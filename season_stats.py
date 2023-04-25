import pandas as pd


def calc_cum_season_res(list_of_obj):
    total_result = 0
    results_per_each_team = {}
    for team in list_of_obj:
        # for sum_round_in
        total_result += team.df['CumResult'][len(team.df)-1]
        results_per_each_team[team.name] = [team.df['CumResult'][len(team.df)-1]]

    return total_result, results_per_each_team
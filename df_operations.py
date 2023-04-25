import pandas as pd

def calc_stakes_uo_results(list_of_obj_teams, model_starting_stake):
    list_of_obj = create_starting_stake_and_ou_result(list_of_obj_teams, model_starting_stake)
    list_of_obj = calculate_stakes(list_of_obj)
    list_of_obj = calc_round_result(list_of_obj)
    list_of_obj = calc_cum_sum(list_of_obj)
    return list_of_obj

def create_starting_stake_and_ou_result(list_of_obj_teams, model_starting_stake):
    for team in list_of_obj_teams:
        team.df['stake'] = 0
        team.df['stake'][0] = model_starting_stake
        team.df['Over2.5'] = team.df.apply(lambda row: 1 if (row['FTHG'] + row['FTAG']) > 2.5 else 0, axis=1)
        print('')
    return list_of_obj_teams

def calculate_stakes(list_of_obj_teams):

    for team in list_of_obj_teams:
        current_stake = -1
        for number in range(len(team.df)):
            if number == 0:
                current_stake = team.df['stake'][0]
                if team.df['Over2.5'][0] == 0:
                    current_stake = current_stake * 2
                continue

            team.df['stake'][number] = current_stake

            if team.df['Over2.5'][number] == 0:
                current_stake = current_stake * 2

            if team.df['Over2.5'][number] == 1:
                current_stake = team.df['stake'][0]

    return list_of_obj_teams

def calc_round_result(list_of_obj_teams):
    for team in list_of_obj_teams:
        team.df['Zysk netto'] = team.df.apply(lambda row: -row['stake'] if row['Over2.5'] == 0 else row['stake'] * (row['BbMx>2.5']-1) , axis=1)
    return list_of_obj_teams

def calc_cum_sum(list_of_obj_teams):
    for team in list_of_obj_teams:
        team.df['CumResult'] = team.df['Zysk netto'].cumsum()
    return list_of_obj_teams


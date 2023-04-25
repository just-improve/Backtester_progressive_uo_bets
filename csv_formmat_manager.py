import pandas as pd
def orgnizer_csv_formatter(csv_all_season_file_name):
    '''it returns list of df where one df represent one team'''
    df = get_formmated_df(csv_all_season_file_name)
    list_of_teams_names = get_list_of_df_teams(df)
    list_of_obj_teams = create_list_obj_teams(list_of_teams_names, df)

    return list_of_obj_teams

def get_formmated_df(cvs_file_name):
    '''it returns formmated df only with columns which you want to use'''
    df = pd.read_csv(cvs_file_name)
    df = df.loc[:, ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'BbMx>2.5', 'BbMx<2.5']]
    return df

def get_list_of_df_teams(df):
    unique_elements = df['HomeTeam'].unique().tolist()
    return unique_elements

def create_list_obj_teams(list_of_teams, df):
    list_of_obj_teams = []

    for team_name in list_of_teams:
        df_team = df.loc[df.eq(team_name).any(axis=1)]
        df_team = df_team.reset_index(drop=True)
        team = Team(team_name, df_team)
        list_of_obj_teams.append(team)

    return list_of_obj_teams

class Team:
    def __init__(self, name, df):
        self.name = name
        self.df = df




# team.df['Over2.5'] = team.df.apply(create_uo_column, axis=1)
# def create_uo_column(df):
#     goals_sum = df['FTHG'] + df['FTAG']
#     if goals_sum > 2.5:
#         return 1
#     else:
#         return 0
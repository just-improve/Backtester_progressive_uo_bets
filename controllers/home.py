import csv_formmat_manager
import df_operations
import season_stats
import plotsy

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.h_sign_in_btn.config(command=self.go_to_sing_in)
        self.frame.h_sign_out_btn.config(command=self.go_to_sing_out)
        self.frame.backtest_btn.config(command=self.controller_method_organizer)
        self.frame.show_teams_stats_btn.config(command=self.show_html_stats)

    def show_html_stats(self):
        plotsy.show_pandas_table_plots(self.model)

    def go_to_sing_in(self):
        self.view.switch('signin')

    def go_to_sing_out(self):
        self.view.switch('signup')

    def controller_method_organizer(self):
        self.store_settings()
        self.model.m_list_of_obj_teams = csv_formmat_manager.orgnizer_csv_formatter(self.model.m_csv_file_name)
        self.model.m_list_of_obj_teams = df_operations.calc_stakes_uo_results(self.model.m_list_of_obj_teams, self.model.m_stake_per_team)
        self.model.season_total_result, self.model.end_result_each_team = season_stats.calc_cum_season_res(self.model.m_list_of_obj_teams)
        self.frame.starting_stake_per_team_lab.config(text=str(self.model.season_total_result))
        print('')

    def store_settings(self):
        self.model.m_csv_file_name = self.frame.e_csv_file.get()
        self.model.m_stake_per_team = int(self.frame.e_stake_per_team.get())

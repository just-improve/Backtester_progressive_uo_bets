from tkinter import Frame, Label, Button, Entry


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        px = 5
        py = 2

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="csv file name")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.e_csv_file = Entry(self)
        self.e_csv_file.grid(row=0, column=1, padx=px, pady=py)
        self.e_csv_file.insert(0, 'pr2010_2011.csv')

        self.starting_stake_per_team_lab = Label(self, text="Stawka startowa na drużyne")
        self.starting_stake_per_team_lab.grid(row=1, column=0, padx=px, pady=py)  # sticky="ew"

        self.e_stake_per_team = Entry(self)
        self.e_stake_per_team.grid(row=1, column=1, padx=px, pady=py)
        self.e_stake_per_team.insert(0, 10)

        self.backtest_btn = Button(self, text="make backtest")
        self.backtest_btn.grid(row=2, column=0, padx=10, pady=10)

        self.show_teams_stats_btn = Button(self, text="show each team stats")
        self.show_teams_stats_btn.grid(row=3, column=0, padx=10, pady=10)

        self.h_sign_in_btn = Button(self, text="Go to Singin View")
        self.h_sign_in_btn.grid(row=4, column=0, padx=10, pady=10)

        self.h_sign_out_btn = Button(self, text="Sign Out")
        self.h_sign_out_btn.grid(row=5, column=0, padx=10, pady=10)


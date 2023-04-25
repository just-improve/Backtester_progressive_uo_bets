import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML, display
import webbrowser
from tempfile import NamedTemporaryFile

def show_pandas_table_plots(model):
    # second file
    print('')
    df = pd.DataFrame([model.end_result_each_team])
    print('')

    html = df.style.set_table_attributes('style="font-size: 12px"').to_html()
    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        f.write(html.encode())
        filepath = f.name
    webbrowser.open('file://' + filepath)


    # all teams df
    for x in model.m_list_of_obj_teams:
        df_team = x.df
        html = df_team.style.set_table_attributes('style="font-size: 12px"').to_html()

        # Save the HTML output to a temporary file
        with NamedTemporaryFile(delete=False, suffix='.html') as f:
            f.write(html.encode())
            filepath = f.name

        # Open the HTML file in the default web browser
        webbrowser.open('file://' + filepath)

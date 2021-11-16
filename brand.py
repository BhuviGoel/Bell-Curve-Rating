import plotly.figure_factory as ff
import pandas as pd
import csv

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Project 108 - Bell Curve\data.csv")

fig = ff.create_distplot([data["Avg Rating"].tolist()], ["rating"], show_hist=False)
fig.show()
import plotly
import plotly.express as px
import pandas as pd
import json

from .api import teamnames, wins, max_points, percentage

df = pd.DataFrame({
    'Wins': wins,
    'Max Points': max_points,
    'Team': teamnames,
    'Percentage of Max Points': percentage
})

points_wins = px.scatter(df, x='Max Points', y='Wins', color='Team')
pw_graph = json.dumps(points_wins, cls=plotly.utils.PlotlyJSONEncoder)

points_percentage = px.scatter(
    df, x='Max Points', y='Percentage of Max Points', color='Team')
pp_graph = json.dumps(points_percentage, cls=plotly.utils.PlotlyJSONEncoder)

wins_percentage = px.scatter(
    df, x='Wins', y='Percentage of Max Points', color='Team')
wp_graph = json.dumps(wins_percentage, cls=plotly.utils.PlotlyJSONEncoder)

import plotly
import plotly.express as px
import pandas as pd
import json

from .api import teamnames, wins, max_points, percentage

# users pandas to create framework of data types for the scatter plots
df = pd.DataFrame({
    'Wins': wins,
    'Max Points': max_points,
    'Team': teamnames,
    'Percentage of Max Points': percentage
})

# scatter plot for max points vs wins
points_wins = px.scatter(df, x='Max Points', y='Wins', color='Team')
pw_graph = json.dumps(points_wins, cls=plotly.utils.PlotlyJSONEncoder)

# scatter plot for max points vs percentage of max points
points_percentage = px.scatter(
    df, x='Max Points', y='Percentage of Max Points', color='Team')
pp_graph = json.dumps(points_percentage, cls=plotly.utils.PlotlyJSONEncoder)

# scatter plot for wins vs percentage of max points
wins_percentage = px.scatter(
    df, x='Wins', y='Percentage of Max Points', color='Team')
wp_graph = json.dumps(wins_percentage, cls=plotly.utils.PlotlyJSONEncoder)

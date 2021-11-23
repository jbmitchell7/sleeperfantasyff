import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

from .api import (teamnames, wins, max_points, percentage,
                  mean_max_points, mean_percentage, mean_wins, actual_points)


def to_percent(int):
    new = "{:.2%}".format(int)
    return new


# users pandas to create framework of data types for the scatter plots
df = pd.DataFrame({
    'Wins': wins,
    'Max Points': max_points,
    'Team': teamnames,
    'Percentage of Max Points': percentage
})


# scatter plot for max points vs wins
points_wins = px.scatter(df, x='Max Points', y='Wins', color='Team')
# adds horizontal mean line
points_wins.add_hline(y=mean_wins, line_width=1, line_dash="dash",
                      annotation_text=f"Mean Wins: {mean_wins}")
# adds vertical mean line
points_wins.add_vline(x=mean_max_points, line_width=1, line_dash="dash",
                      annotation_text=f"Mean Max Points: {mean_max_points}")
pw_graph = json.dumps(points_wins, cls=plotly.utils.PlotlyJSONEncoder)

# scatter plot for max points vs percentage of max points
points_percentage = px.scatter(
    df, x='Max Points', y='Percentage of Max Points', color='Team')
# adds horizontal mean line
points_percentage.add_hline(y=mean_percentage, line_width=1, line_dash="dash",
                            annotation_text=f"Mean Percentage: {to_percent(mean_percentage)}")
points_percentage.update_yaxes(tickformat=".0%")
# adds vertical mean line
points_percentage.add_vline(x=mean_max_points, line_width=1, line_dash="dash",
                            annotation_text=f"Mean Max Points: {mean_max_points}")
pp_graph = json.dumps(points_percentage, cls=plotly.utils.PlotlyJSONEncoder)

### scatter plot for wins vs percentage of max points ###
wins_percentage = px.scatter(
    df, x='Wins', y='Percentage of Max Points', color='Team')
# adds horizontal mean line
wins_percentage.add_hline(y=mean_percentage, line_width=1, line_dash="dash",
                          annotation_text=f"Mean Percentage: {to_percent(mean_percentage)}")
wins_percentage.update_yaxes(tickformat=".0%")
# adds vertical mean line
wins_percentage.add_vline(x=mean_wins, line_width=1, line_dash="dash",
                          annotation_text=f"Mean Wins: {mean_wins}")
wp_graph = json.dumps(wins_percentage, cls=plotly.utils.PlotlyJSONEncoder)


def percent_convert(arr):
    new_arr = []
    for i in arr:
        new_arr.append(to_percent(i))
    return new_arr


standings = go.Figure(data=[go.Table(
    header=dict(values=["Team", "Wins", "Points Scored",
                "Max Points", "Percentage of Max Points"]),
    cells=dict(values=[teamnames, wins, actual_points,
               max_points, percent_convert(percentage)])
)
])
standings_graph = json.dumps(standings, cls=plotly.utils.PlotlyJSONEncoder)

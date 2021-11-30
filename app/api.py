import requests
import numpy as np


### api url call ###
def api_get(url_param, league_id):
    return requests.get(f'https://api.sleeper.app/v1/league/{league_id}/{url_param}')


### leagues ###
loeg = '720397292238073856'
sloppy_joes = '725424222041657344'


# will eventually allow user to toggle league choice
def change_league(league):
    roster_list = api_get("rosters", league).json()
    user_list = api_get("users", league).json()
    league_data = [roster_list, user_list]
    return league_data


# initializes league data
league_data = change_league(sloppy_joes)
#league_data = change_league(loeg)


### api keys ###
# user_id - user['user_id']
# id - roster['owner_id']
# teamname - user['display_name']
# wins - roster['settings']['wins']
# max points - roster['settings']['ppts']
# actual points - roster['settings']['fpts']


# gets team name
def get_name(owners, users):
    names = []
    for owner in owners:
        for user in users:
            if owner['owner_id'] == user['user_id']:
                names.append(user['display_name'])
    return names


# gets various team stats(wins, actual points, max points)
# based on input
def get_stats(res, stat):
    stat_arr = []
    for team in res:
        data = team['settings'][stat]
        stat_arr.append(data)
    return stat_arr


def get_mean(input):
    mean_input = np.mean(input)
    return mean_input


teamnames = get_name(league_data[0], league_data[1])
wins = get_stats(league_data[0], 'wins')

max_points = get_stats(league_data[0], 'ppts')
actual_points = get_stats(league_data[0], 'fpts')
# uses numpy to divide actual and
# max point arrays and get total point percentage
mp = np.array(max_points)
ap = np.array(actual_points)
percentage = ap/mp

mean_max_points = get_mean(max_points)
mean_wins = get_mean(wins)
mean_percentage = get_mean(percentage)

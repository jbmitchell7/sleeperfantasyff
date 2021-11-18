import requests
import numpy as np

league_id = '720397292238073856'


def api_get(url_param):
    return requests.get(f'https://api.sleeper.app/v1/league/{league_id}/{url_param}')


rosters = api_get("rosters").json()
users = api_get("users").json()

# id - roster['owner_id']
# wins - roster['settings']['wins']
# max points - roster['settings']['ppts']
# actual points - roster['settings']['fpts']


def get_teamnames(res):
    teams = []
    for team in res:
        username = team['display_name']
        teams.append(username)
    return teams


def get_owner_id(res):
    owners = []
    for owner in res:
        id = owner['owner_id']
        owners.append(id)
    return owners


def get_stats(res, stat):
    stat_arr = []
    for team in res:
        data = team['settings'][stat]
        stat_arr.append(data)
    return stat_arr


def convert_percent(arr):
    new_arr = []
    for i in arr:
        new_i = "{:.2%}".format(i)
        new_arr.append(new_i)
    return new_arr


teamnames = get_teamnames(users)
ids = get_owner_id(rosters)
wins = get_stats(rosters, 'wins')

max_points = get_stats(rosters, 'ppts')
actual_points = get_stats(rosters, 'fpts')
mp = np.array(max_points)
ap = np.array(actual_points)
percentage = ap/mp

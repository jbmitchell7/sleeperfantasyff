import requests
import numpy as np

loeg = '720397292238073856'
sloppy_joes = '725424222041657344'


def api_get(url_param):
    return requests.get(f'https://api.sleeper.app/v1/league/{sloppy_joes}/{url_param}')


rosters = api_get("rosters").json()
users = api_get("users").json()
#
# user_id - user['user_id']
# id - roster['owner_id']
# teamname - user['display_name']
# wins - roster['settings']['wins']
# max points - roster['settings']['ppts']
# actual points - roster['settings']['fpts']


def get_name(owners, users):
    names = []
    for owner in owners:
        for user in users:
            if owner['owner_id'] == user['user_id']:
                names.append(user['display_name'])
    return names


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


teamnames = get_name(rosters, users)
wins = get_stats(rosters, 'wins')

max_points = get_stats(rosters, 'ppts')
actual_points = get_stats(rosters, 'fpts')
mp = np.array(max_points)
ap = np.array(actual_points)
percentage = ap/mp

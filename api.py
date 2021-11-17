import requests

league_id = '720397292238073856'


def api_get(url_param):
    return requests.get(f'https://api.sleeper.app/v1/league/{league_id}/{url_param}')


rosters = api_get("rosters").json()
users = api_get("users").json()

# need to get from rosters:
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


print(get_teamnames(users))

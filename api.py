import requests
import json

response = requests.get('https://api.sleeper.app/v1/league/720397292238073856/rosters')

data = response.json()

def get_owners(res):
    teams = []
    for team in res:
        owner = team.get('owner_id')
        teams.append(owner)
    return teams

print(get_owners(data))

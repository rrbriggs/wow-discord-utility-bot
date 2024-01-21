from ninja import NinjaAPI
from config import BATTLENET_SECRET_KEY, BATTLENET_ID
from django.http import JsonResponse
import json
import logging
from pprint import pprint
import requests


logger = logging.getLogger("wow-bot")

api = NinjaAPI()

@api.get("/mythic")
def get_mythic_plus_info(request):
    access_token_response = create_access_token()
    if access_token_response.status_code != 200:
        logger.warn(f"bnet access token request failed: {access_token_response}")
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)

    access_token = access_token_response.json().get('access_token')
    logger.info(f"bnet access token: {access_token}")
    guild_roster_response = get_guild_roster(access_token=access_token, guild_slug='sleepless-kingdom')

    members = get_members_by_rank(guild_roster_response.json())

def create_access_token():
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://us.battle.net/oauth/token', data=data, auth=(BATTLENET_ID, BATTLENET_SECRET_KEY))
    return response

def get_guild_roster(access_token: str, guild_slug: str, server_slug: str = 'area-52', region: str = 'us', namespace: str = 'profile-us', locale: str = 'en_US'):
    params = { 
        'region': region,
        'namespace': namespace,
        'locale': locale,
        'access_token': access_token,
        }
    url = f'https://us.api.blizzard.com/data/wow/guild/{server_slug}/{guild_slug}/roster'
    print(url)
    response = requests.get(f'https://us.api.blizzard.com/data/wow/guild/{server_slug}/{guild_slug}/roster', params=params)
    return response

def get_members_by_rank(guild_roster_json: json):
    members = guild_roster_json.get('members', [])

    #TODO: {guild_ranks_to_consider} will need to be moved to get stored in the DB, and get set by the user on startup
    #TODO: also this needs to be able to be modified if the guild ranks are changed, or the user messed up
    guild_ranks_to_consider = [0, 1, 2, 3]
    selected_members = [member for member in members if member.get('rank') in guild_ranks_to_consider]
    pprint(selected_members)

    return selected_members

from config import BATTLENET_SECRET_KEY, BATTLENET_ID
from wowbot.bnet_token_repo import get_access_token
import json
from pprint import pprint
import requests
import logging

logger = logging.getLogger("wow-bot")

def create_access_token():
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://us.battle.net/oauth/token', data=data, auth=(BATTLENET_ID, BATTLENET_SECRET_KEY))
    if response.status_code != 200:
            logger.warn(f"bnet access token request failed: {response}")
            return None

    token = response.json().get('access_token')
    if token is not None:
        logger.info(f"bnet access token created: {token}")

    return token

#perhaps having an enum to match some of these server-slugs, namespaces etc against would be where it's at
def get_guild_roster(guild_slug: str, server_slug: str = 'area-52', region: str = 'us', namespace: str = 'profile-us', locale: str = 'en_US'):
    token = get_access_token()

    # TODO: return something useful here sometime
    if token is None: 
        return None
    
    params = { 
        'region': region,
        'namespace': namespace,
        'locale': locale,
        'access_token': token,
        }
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

def get_mythic_keystone_season(region: str = "us", namespace: str = "profile-us", locale: str = "en-us"):
    token = get_access_token()

    # TODO: return something useful here sometime
    if token is None: 
        return None

    params = {
        "region": ""
    }

# def get_mythic_keystone_by_character():
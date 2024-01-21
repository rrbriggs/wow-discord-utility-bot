from ninja import NinjaAPI
from config import BATTLENET_SECRET_KEY, BATTLENET_ID
from django.http import JsonResponse
import requests
import logging

logger = logging.getLogger(__name__)

api = NinjaAPI()

@api.get("/mythic")
def get_mythic_plus_info(request):
    access_token_request = create_access_token()
    if access_token_request.status_code != 200:
        logger.warn(f"bnet access token request failed: {access_token_request}")
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)

    access_token = access_token_request.json().get('access_token')
    logger.info(f"bnet access token: {access_token}")
    guild_roster = get_guild_roster(access_token=access_token, guild_slug='sleepless-kingdom')

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
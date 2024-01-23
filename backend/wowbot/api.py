from ninja import NinjaAPI
from django.http import JsonResponse
from wowbot.blizzard_api_service import create_access_token, get_guild_roster, get_members_by_rank
import logging

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
    


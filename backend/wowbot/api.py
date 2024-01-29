from ninja import NinjaAPI
from wowbot.blizzard_api_service import get_guild_roster, get_members_by_rank
from wowbot.guild_character_repo import add_or_update_characters
import logging

logger = logging.getLogger("wow-bot")

api = NinjaAPI()

@api.get("/mythic")
def get_mythic_plus_info(request, guild_name: str):
    transformed_guild_name = guild_name.strip().lower()

    # get roster from bnet
    guild_roster_response = get_guild_roster(guild_slug=transformed_guild_name)
    # lets snag everyone from rank 0, 1, 2, 3
    # TODO: this needs to be user set via discord bot in the future
    members = get_members_by_rank(guild_roster_response.json())
    # we dropped everyone into the DB then return a set() of those users
    ranked_members = add_or_update_characters(members)
    # time to snag mythic dungeon info for these characters
    
    
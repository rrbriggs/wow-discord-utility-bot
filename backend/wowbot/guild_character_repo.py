from wowbot.models import Characters
from django.db import IntegrityError
import logging

logger = logging.getLogger("wow-bot")

def add_or_update_characters(members: list):
    for member_data in members:
        member_info = member_data['character']
        member_rank = member_data['rank']
        character = None
        created = None

        lookup_params = {'id': member_info['id']}
        defaults = {
            'key_href': member_info['key']['href'],
            'level': member_info['level'],
            'name': member_info['name'],
            'playable_class_id': member_info['playable_class']['id'],
            'playable_class_href': member_info['playable_class']['key']['href'],
            'playable_race_id': member_info['playable_race']['id'],
            'playable_race_href': member_info['playable_race']['key']['href'],
            'realm_id': member_info['realm']['id'],
            'realm_key_href': member_info['realm']['key']['href'],
            'realm_slug': member_info['realm']['slug'],
            'rank': member_rank,
            'meta': None
        }

        try: 
            character, created = Characters.objects.update_or_create(
                defaults = defaults, **lookup_params
            )
            if created:
                logger.info(f"Created character with name and id of: {character.name} - {character.id}")
            else:
                logger.info(f"Character: {character.name} - {character.id} already existed, attempted to update")
        except Exception as err:
            logger.info(f"Something bad happened while trying to update_or_create for this character: {member_info['name']} - {member_info['id']}")

        



        
from wowbot.models import Character

#
def addCharacters(members: list):
    for member_data in members:
        member_info = member_data['character']
        member_rank = member_data['rank']

        # Create a new Character instance
        new_character = Character(
            id = member_info['id'],
            key_href = member_info['key']['href'],
            level = member_info['level'],
            name = member_info['name'],

            playable_class_id = member_info['playable_class']['id'],
            playable_class_href = member_info['playable_class']['key']['href'],

            playable_race_id = member_info['playable_race']['id'],
            playable_race_href = member_info['playable_race']['key']['href'],

            realm_id = member_info['realm']['id'],
            realm_key_href = member_info['realm']['key']['href'],
            realm_slug = member_info['realm']['slug'],

            rank = member_rank,

            meta = None,
        )

        new_character.save()
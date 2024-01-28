from wowbot.models import BnetTokens
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger("wow-bot")

# we're just going to always call get_access_token() and let it handle any cases
# there is no point where we're going to want to get a token and not create a new one
# if it doesn't exist or needs to be updated
def get_access_token():
    try:
        token = BnetTokens.objects.all().order_by('id').first()
        if token is None: 
            logger.info("Token did not exist in DB, it's time to pick up a new one")
            token = create_bnet_access_token()
            
        if timezone.now() - token.date > timedelta(days=1):
            token.delete()
            logger.warn("Token out of date, deleting the old and attempting to get a new one..")
            token = create_bnet_access_token()
        return token
    except Exception as e: 
        logger.warn("There was an error getting a token from the DB: {e}")
        return None
    
def create_bnet_access_token():
    from wowbot.blizzard_api_service import create_access_token
    logger.info("Creating a new token")
    token = create_access_token()

    defaults = {
        "token": token,
    }

    token = BnetTokens.objects.create(**defaults)
    return token
from django.db import models

#Character from bliz api Guild Roster
class Characters(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    key_href = models.URLField()
    level = models.IntegerField(blank=True)
    name = models.CharField(max_length=100, db_index=True)
    
    playable_class_id = models.IntegerField()
    playable_class_href = models.URLField()
    
    playable_race_id = models.IntegerField()
    playable_race_href = models.URLField()
    
    realm_id = models.IntegerField()
    realm_key_href = models.URLField()
    realm_slug = models.CharField(max_length=100)
    
    rank = models.IntegerField()

    meta = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class BnetTokens(models.Model):
    token = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.token

class CharacterDungeons(models.Model):
    player_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    realm_slug = models.CharField(max_length=100)
    mplus_rating = models.FloatField()
    affixes = models.JSONField(null=True, blank=True)
    best_runs = models.JSONField(null=True, blank=True)
    previous_best = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.player_id
    
class DungeonIdAssociation(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id
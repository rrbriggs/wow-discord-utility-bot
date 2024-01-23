from django.db import models

#Character from bliz api Guild Roster
class Character(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    key_href = models.URLField()
    level = models.IntegerField()
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

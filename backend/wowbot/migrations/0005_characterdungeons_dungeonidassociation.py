# Generated by Django 5.0.1 on 2024-01-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowbot', '0004_bnettokens_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterDungeons',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('realm_slug', models.CharField(max_length=100)),
                ('mplus_rating', models.FloatField()),
                ('affixes', models.JSONField(blank=True, null=True)),
                ('best_runs', models.JSONField(blank=True, null=True)),
                ('previous_best', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DungeonIdAssociation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

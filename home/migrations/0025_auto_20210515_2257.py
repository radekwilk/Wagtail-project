# Generated by Django 3.1.8 on 2021-05-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210504_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleaguedetail',
            name='games_played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teamleaguedetail',
            name='goals_diff',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teamleaguedetail',
            name='league_position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teamleaguedetail',
            name='points',
            field=models.IntegerField(),
        ),
    ]

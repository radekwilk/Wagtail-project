# Generated by Django 3.1.8 on 2021-04-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210429_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnewspost',
            name='post_text',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]

# Generated by Django 3.1.8 on 2021-04-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210429_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportnewspost',
            name='post_type',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

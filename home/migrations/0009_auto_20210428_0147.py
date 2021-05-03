# Generated by Django 3.1.8 on 2021-04-28 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0008_homepage_bg_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='card_image_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card_image_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card_title_1',
            field=models.CharField(default='Card 1', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card_title_2',
            field=models.CharField(default='Card 2', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card_title_3',
            field=models.CharField(default='Card 3', max_length=100),
        ),
    ]

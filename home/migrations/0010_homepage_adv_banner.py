# Generated by Django 3.1.8 on 2021-04-28 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0009_auto_20210428_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='adv_banner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]

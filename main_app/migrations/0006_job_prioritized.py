# Generated by Django 2.2 on 2019-06-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190618_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='prioritized',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.2 on 2019-06-20 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20190620_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
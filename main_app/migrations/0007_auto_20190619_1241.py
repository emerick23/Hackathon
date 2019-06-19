# Generated by Django 2.2 on 2019-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_job_prioritized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='prioritized',
            field=models.CharField(choices=[('T', -1), ('F', 1)], default='T', max_length=1),
        ),
    ]

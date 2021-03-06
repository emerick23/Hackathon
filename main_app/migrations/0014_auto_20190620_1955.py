# Generated by Django 2.2 on 2019-06-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20190620_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='stage',
            field=models.CharField(choices=[('A', 'Apply'), ('I', 'Interview'), ('F', 'Follow Up'), ('O', 'Outcomes')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='types',
            field=models.CharField(choices=[('I', 'Internship'), ('C', 'Contract'), ('P', 'Part-Time'), ('F', 'Full-Time')], default='I', max_length=10),
        ),
    ]

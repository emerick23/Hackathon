# Generated by Django 2.2 on 2019-06-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190618_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Job')),
            ],
        ),
    ]

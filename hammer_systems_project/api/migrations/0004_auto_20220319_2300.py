# Generated by Django 2.2.16 on 2022-03-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220319_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default={'n?vI'}, editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default={'"+1-=7'}, editable=False, max_length=6),
        ),
    ]
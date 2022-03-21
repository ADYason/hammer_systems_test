# Generated by Django 2.2.16 on 2022-03-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220319_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default={'18AD'}, editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default={'A80033'}, editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
# Generated by Django 2.2.16 on 2022-03-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220319_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default={'A2aA'}, editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default={'Dac6Fe'}, editable=False, max_length=6),
        ),
    ]

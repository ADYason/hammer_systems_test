# Generated by Django 2.2.16 on 2022-03-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20220321_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='b304', editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default='fC852a', editable=False, max_length=6),
        ),
    ]

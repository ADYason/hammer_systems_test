# Generated by Django 2.2.16 on 2022-03-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220319_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confermed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default={'94d2'}, editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default={'673D61'}, editable=False, max_length=6),
        ),
    ]

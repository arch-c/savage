# Generated by Django 4.0.1 on 2022-01-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savage_bcw', '0003_rename_member_game_members_member_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='games',
        ),
        migrations.AlterField(
            model_name='game',
            name='members',
            field=models.ManyToManyField(related_name='games', to='savage_bcw.Member'),
        ),
    ]

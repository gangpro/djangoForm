# Generated by Django 2.2.2 on 2019-06-19 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_board_like_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='like_user',
            new_name='like_users',
        ),
    ]
# Generated by Django 4.1.5 on 2023-02-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_rename_comment_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='viewers',
            new_name='seen_by',
        ),
    ]

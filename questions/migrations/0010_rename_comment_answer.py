# Generated by Django 4.1.5 on 2023-02-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_alter_topic_viewers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Answer',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-26 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_remove_topic_comments_topic_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='answers',
        ),
    ]

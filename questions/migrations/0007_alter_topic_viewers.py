# Generated by Django 4.1.5 on 2023-02-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_topic_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='viewers',
            field=models.JSONField(default={}),
        ),
    ]

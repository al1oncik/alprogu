# Generated by Django 4.1.5 on 2023-02-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_alter_topic_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
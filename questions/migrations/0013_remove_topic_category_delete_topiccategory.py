# Generated by Django 4.1.5 on 2023-02-19 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_topiccategory_topic_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.DeleteModel(
            name='TopicCategory',
        ),
    ]
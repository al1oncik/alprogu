# Generated by Django 4.1.5 on 2023-03-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_remove_topic_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.CharField(default='undefined', max_length=150),
        ),
    ]

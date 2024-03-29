# Generated by Django 4.1.5 on 2023-02-26 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_rename_answer_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='topic',
        ),
        migrations.AddField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='users_voted',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='comments',
            field=models.JSONField(default=list),
        ),
    ]

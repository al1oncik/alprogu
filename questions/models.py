from django.db import models
from users.models import User


class Topic(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    creator = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    users_voted = models.JSONField(default=list)
    comments = models.ManyToManyField('Comment', blank=True)
    views = models.IntegerField(default=0)
    seen_by = models.JSONField(default=list)
    categories = models.JSONField(default=list)

    @property
    def answers(self):
        return self.comments.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    creator = models.CharField(max_length=150, default="undefined")
    vote = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    users_voted = models.JSONField(default=list)
    def __str__(self):
        return self.text

    def get_image(self):
        return User.objects.get(username=self.creator).image

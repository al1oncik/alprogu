from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    creator = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    answers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    seen_by = models.JSONField(default=list)
    categories = models.JSONField(default=list)

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

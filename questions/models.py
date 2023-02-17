from django.db import models
from django.utils import timezone

class Topic(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    creator = models.CharField(max_length=150)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def created(self):
        t = timezone.now() - self.creation_date
        return f"{t.days} days"

class Comment(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

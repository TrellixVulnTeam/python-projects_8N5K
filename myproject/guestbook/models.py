from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'<Name: {self.name}, ID: {self.id}>'
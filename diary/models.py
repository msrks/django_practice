from django.db import models
from django.utils import timezone

class Day(models.Model):
    title = models.CharField('title', max_length=200)
    text = models.TextField('main text')
    date = models.DateTimeField('datetime', default=timezone.now)

    def __str__(self):
        return self.title
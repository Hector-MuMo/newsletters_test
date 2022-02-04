from django.db import models
from tags.models import Tag
from newsusers.models import User


class Newsletter(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    target = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='newsletter')
    author = models.ForeignKey(User, related_name='author_news', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='suscriber_news')
    voters = models.ManyToManyField(User, related_name='voters_news')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

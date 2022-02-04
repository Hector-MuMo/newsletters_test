from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

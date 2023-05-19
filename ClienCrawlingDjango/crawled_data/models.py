from django.db import models


class BoardData(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField()
    specific_id = models.CharField(max_length=15)


# Create your models here.

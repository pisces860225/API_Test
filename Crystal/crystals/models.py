from django.db import models

# Create your models here.
class Crystal(models.Model):
    category = models.TextField()
    weight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    origin = models.TextField()
    title = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = "crystals"
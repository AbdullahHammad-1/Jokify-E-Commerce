from django.db import models

# Create your models here.


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    dis_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title

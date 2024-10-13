from django.db import models
import json
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


class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    items = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_items(self):
        """Deserialize the items field."""
        return json.loads(self.items)

    def set_items(self, items):
        """Serialize items into JSON format."""
        self.items = json.dumps(items)

    def __str__(self):
        return self.name

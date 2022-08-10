from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://prom-marker.ru/components/com_jshopping/files/img_products/Prom-marker_piktogramma-kafe-restoran-nastennaya-tablichka-durable-diametr-83mm-4909-23.jpg")

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})





from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=30)


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=30)


class Shoe(models.Model):
    size = models.IntegerField()
    brandname = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)

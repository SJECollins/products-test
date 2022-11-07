from django.db import models

class BaseProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    current_stock = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    added_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class ProductSizes(models.Model):
    size = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.size


class Seed(BaseProduct):
    time_to_maturity = models.CharField(max_length=140, null=True, blank=True)
    flavour = models.CharField(max_length=140, null=True, blank=True)
    scovilles = models.CharField(max_length=140, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Sauce(BaseProduct):
    ingredients = models.CharField(max_length=255, null=True, blank=True)
    heat_level = models.CharField(max_length=20, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class SeedBox(BaseProduct):
    seeds = models.ManyToManyField(Seed)
    price = models.ManyToManyField(ProductSizes)

    class Meta:
        verbose_name_plural = 'Seed Boxes'


class SauceBox(BaseProduct):
    sauces = models.ManyToManyField(Sauce)
    price = models.ManyToManyField(ProductSizes)

    class Meta:
        verbose_name_plural = 'Sauce Boxes'
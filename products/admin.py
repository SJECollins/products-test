from django.contrib import admin

from .models import ProductSizes, Seed, Sauce, SeedBox, SauceBox


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_filter = ('name', 'current_stock',)
    list_display = ('name', 'current_stock', 'in_stock',)
    search_fields = ('name',)


@admin.register(SeedBox)
class SeedBoxAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'in_stock',)
    search_fields = ('name',)


admin.site.register(ProductSizes)
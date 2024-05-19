from django.contrib import admin
from django.apps import apps
from django.db import models

# Avval barcha modellarni olish
app = apps.get_app_config('customadmin')

# Har bir model uchun maxsus admin klassi yaratish
for model_name, model in app.models.items():
    # Dinamik tarzda admin klassini yaratish
    class CustomAdmin(admin.ModelAdmin):
        # Qidiruv maydonlari
        search_fields = [field.name for field in model._meta.fields if isinstance(field, (models.CharField, models.TextField))]
        
        # List display
        list_display = [field.name for field in model._meta.fields]
        
        # List filter
        list_filter = [field.name for field in model._meta.fields if isinstance(field, (models.BooleanField, models.DateField, models.ForeignKey))]

        # Ordering
        ordering = [model._meta.pk.name]

    # Klassga nom berish
    CustomAdmin.__name__ = f'{model_name}Admin'
    
    # Admin saytida ro'yxatdan o'tkazish
    admin.site.register(model, CustomAdmin)
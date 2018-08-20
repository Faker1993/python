from django.contrib import admin
from super import models

# Register your models here.
@admin.register(models.Item)
class Itemadmin(admin.ModelAdmin):
    list_display = ('text',)
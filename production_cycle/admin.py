from django.contrib import admin
from production_cycle import models

# Register your models here.
admin.site.register(models.Day)
admin.site.register(models.Cycle)
admin.site.register(models.Standards)

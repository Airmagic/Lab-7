from django.contrib import admin
from .models import Place

# Register your models here
# this makes it so you can manage the date in the db
admin.site.register(Place)

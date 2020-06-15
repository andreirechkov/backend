from django.contrib import admin
from .models import News, Person

admin.site.register(Person)
admin.site.register(News)

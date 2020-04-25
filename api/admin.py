from django.contrib import admin
from .models import Test, Person

admin.site.register(Person)
admin.site.register(Test)

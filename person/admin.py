from django.contrib import admin
from person.models import Person,Country,City
# Register your models here.
admin.site.register([Person, Country, City])
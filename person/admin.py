from django.contrib import admin
from person.models import Consumer,Zone,Division,SubDivision
# Register your models here.
admin.site.register([Consumer,Zone,Division,SubDivision])
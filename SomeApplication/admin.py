from django.contrib import admin
from SomeApplication.models import Company, Person, Incident

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Incident)

# Register your models here.

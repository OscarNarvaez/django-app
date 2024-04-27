from django.contrib import admin
from .models import User, IdentificationType, Country, Department, City, Person, Student

admin.site.register(User)
admin.site.register(IdentificationType)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Student)

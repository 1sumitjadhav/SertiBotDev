# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Student, university
#from .models import User
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(university)
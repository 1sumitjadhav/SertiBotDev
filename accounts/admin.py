# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Student, university
<<<<<<< HEAD
#from .models import User
# Register your models here.

admin.site.register(User)
=======
# from .models import User
# Register your models here.


>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
admin.site.register(Student)
admin.site.register(university)
<<<<<<< HEAD


from django.urls import path
from .import views

# Create your views here.
urlpatterns =[
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('WELCOME',views.welcome,name='WELCOME'),
    path('Register',views.register,name='Register'),
    path('student/', views.student_register.as_view(), name='student'),
    path('university/', views.university_register.as_view(), name='university'),
    path('success',views.success,name='success'),
]
=======
from django.urls import path
from .views import login_user, register, student_register, university_register, logout_user

# Create your views here.
urlpatterns =[
    path('login', login_user,name='login'),
    path('register', register,name='register'),
    path('student/', student_register.as_view(), name='student'),
    path('university/', university_register.as_view(), name='university'),
    path('logut', logout_user , name='logout_user'),
]
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d

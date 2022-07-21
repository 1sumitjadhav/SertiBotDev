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


from django.urls import path
from .import views

# Create your views here.
urlpatterns =[
    path('login',views.login_user,name='login'),
    path('Register',views.register,name='Register'),
    path('student/', views.student_register.as_view(), name='student'),
    path('university/', views.university_register.as_view(), name='university')
]
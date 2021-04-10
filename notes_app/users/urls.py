from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'  # ye zarrori hai namespace use krne ke liye
urlpatterns =[
    path('login/',views.login,name='login')
]

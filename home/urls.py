from django.urls import path
from . import views

urlpatterns = [
    path('',views.GreetView.as_view(), name='index.home'),
    path('login/', views.LoginInterfaceView.as_view(), name='login.view'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout.view'),
    path('signup/', views.SignupView.as_view(), name='signup.view')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.req, name = 'vlearn'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name = 'login'),
    path('home/', views.homereq, name = 'home'),
    path('logout/', views.logoutuser, name = 'logout')
]   
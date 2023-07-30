from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home,name='home'),
    path('register', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('new',views.new,name='new'),
    path('logout',views.logout,name="logout"),
    path('form', views.form, name='form'),
]


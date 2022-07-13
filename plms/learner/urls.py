from django.urls import path
from learner import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('course/', views.index, name='index'),
    path('', views.userlogin, name='login'),
    path("course/enroll/<int:id>/", views.enroll, name = 'enroll'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('succen', views.succen, name='succen'),
    path('unsuccen', views.unsuccen, name='unsuccen'),
    path('course/enroll/<int:id>/senroll/', views.senroll, name='senroll'),


]
from django.urls import path
from learner import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('course/', views.index, name='index'),
    path('ecourse/', views.eindex, name='eindex'),
    path('', views.home, name='homepage'),
    path("course/enroll/<int:id>/", views.enroll, name = 'enroll'),
    path('ecourse/resources/<int:id>', views.resources, name='resources'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('succen', views.succen, name='succen'),
    path('unsuccen', views.unsuccen, name='unsuccen'),
    path('course/enroll/<int:id>/senroll/', views.senroll, name='senroll'),


]
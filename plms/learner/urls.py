from django.urls import path
from learner import views

urlpatterns = [
    path('homes', views.homes, name='homes'),
    path('homet', views.homet, name='homet'),
    path('course/', views.index, name='index'),
    path('ecourse/', views.eindex, name='eindex'),
    path('tcourse/', views.indext, name='indext'),
    path('add/', views.add, name='add'),
    path('add/addcourse/', views.addcourse, name='addcourse'),
    path('', views.userlogin, name='homepage'),
    path("course/enroll/<int:id>/", views.enroll, name = 'enroll'),
    path('ecourse/resources/<int:id>', views.resources, name='resources'),
    path('register', views.rhome, name='register'),
    path('registers', views.registers, name='registers'),
    path('registert', views.registert, name='registert'),
    path('login', views.userlogin, name='userlogin'),
    path('logout', views.userlogout, name='userlogout'),
    path('succen', views.succen, name='succen'),
    path('unsuccen', views.unsuccen, name='unsuccen'),
    path('course/enroll/<int:id>/senroll/', views.senroll, name='senroll'),
    path('tcourse/updatec/<int:id>', views.updatec, name='updatec'),
    path('tcourse/updatec/<int:id>/updatecdata/', views.updatecdata, name='updatecdata'),


]
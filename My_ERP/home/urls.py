from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addcourse', views.addcourse),
    path('showcourse', views.showcourse),
    path('showstudent', views.showstudent),


]


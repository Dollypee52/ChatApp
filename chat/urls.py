from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # dynamic url i.e whatever url a user goes to, its going to be seen as a room
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

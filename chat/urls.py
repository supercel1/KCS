from . import views
from django.urls import path, include

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

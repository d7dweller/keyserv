from django.urls import path

from . import views

app_name = "keyserv"
urlpatterns = [
    path('', views.index, name="index"),
    path('keys/', views.keys, name="keys"),
    path('key/<int:key_id>/', views.key_deets, name="key_deets"),
    path('key/upload/', views.key_upload, name="key_upload"),
    path('messages/', views.messages, name="messages"),
    path('message/upload/', views.message_upload, name="message_upload"),
    path('message/<int:mess_id>/', views.message_deets, name="message_deets"),

]

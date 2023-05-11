from django.contrib import admin
from django.urls import path
  
# importing views from views..py
from .views import chat_bot
from .views import chat_json_response
  
urlpatterns = [
    path('', chat_bot, name='index'),
    path('chat_bot/', chat_bot, name='chat_bot'),
    path('chat_json_response/', chat_json_response, name='chat_json_response')
]

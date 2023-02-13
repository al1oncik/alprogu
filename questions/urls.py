from django.urls import path
from .views import create, question

app_name = 'questions'

urlpatterns = [
    path('create/', create, name='create'),
    path('question/<int:id>/', question, name='question')
]
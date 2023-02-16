from django.urls import path
from .views import question

app_name = 'questions'

urlpatterns = [
    path('question/<int:id>/', question, name='question')
]
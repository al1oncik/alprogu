from django.urls import path

from .views import question, vote

app_name = 'questions'

urlpatterns = [
    path('question/<int:id>/', question, name='question'),
    path('vote/<int:id>/<str:vote>/', vote, name='vote'),
]
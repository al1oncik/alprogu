from django.urls import path

from .views import question, create, vote

app_name = 'questions'

urlpatterns = [
    path('question/<int:id>/', question, name='question'),
    path('question/create/', create, name='create'),
    path('vote/<int:id>/<str:vote>/', vote, name='vote'),
]
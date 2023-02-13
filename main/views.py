from django.shortcuts import render
from questions.models import Topic

def index(request):
    context = {'topics': Topic.objects.order_by('-id')}
    return render(request, 'main/base.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



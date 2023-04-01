from django.shortcuts import HttpResponseRedirect, render
from django.core.paginator import Paginator

from questions.forms import QuestionCreateForm
from questions.models import Topic


def index(request, page=1):
    paginator = Paginator(Topic.objects.order_by('-id'), 20)

    if request.method == "GET":
        if 'Newest' in request.GET:
            paginator = Paginator(Topic.objects.order_by('-id'), 20)
        if 'Popular' in request.GET:
            paginator = Paginator(Topic.objects.order_by('-views'), 20)
        if 'Vote' in request.GET:
            paginator = Paginator(Topic.objects.order_by('-vote'), 20)

        if "search" in request.GET:
            topics = Topic.objects.filter(title__icontains=request.GET['search'])
            paginator = Paginator(topics, 20)


    context = {'topics': paginator.get_page(page),
               'page': page}
    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



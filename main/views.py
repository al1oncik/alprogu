from django.shortcuts import HttpResponseRedirect, render
from django.core.paginator import Paginator

from questions.forms import QuestionCreateForm
from questions.models import Topic


def index(request, page=1):
    paginator = Paginator(Topic.objects.order_by('-id'), 20)
    if request.method == "POST":
        form = QuestionCreateForm(data=request.POST)
        if form.is_valid():
            Topic.objects.create(
                title=request.POST['title'],
                text=request.POST['text'],
                creator=request.user.username,
            )
            return HttpResponseRedirect('/')
    else:
        form = QuestionCreateForm()
    if request.method == "GET":
        if "sorting" in request.GET:
            if request.GET['sorting'] == "Newest":
                paginator = Paginator(Topic.objects.order_by('-id'), 20)
            if request.GET['sorting'] == "Popular":
                paginator = Paginator(Topic.objects.order_by('-views'), 20)
            if request.GET['sorting'] == "Vote":
                paginator = Paginator(Topic.objects.order_by('-vote'), 20)

        if "search" in request.GET:
            topics = Topic.objects.filter(title__icontains=request.GET['search'])
            paginator = Paginator(topics, 20)


    context = {'topics': paginator.get_page(page),
               'form': form,
               'page': page}
    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



from django.shortcuts import HttpResponseRedirect, render
from django.core.paginator import Paginator

from questions.forms import QuestionCreateForm
from questions.models import Topic


def index(request, page=1):
    paginator = Paginator(Topic.objects.order_by('-id'), 7)
    if request.method == "POST":
        if request.POST['sorting']:
            if request.POST['sorting'] == "Newest":
                paginator = Paginator(Topic.objects.order_by('-id'), 7)
            if request.POST['sorting'] == "Popular":
                paginator = Paginator(Topic.objects.order_by('-views'), 7)
            if request.POST['sorting'] == "Vote":
                paginator = Paginator(Topic.objects.order_by('-vote'), 7)

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

    context = {'topics': paginator.get_page(page),
               'form': form,
               'page': page}
    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



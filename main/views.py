from django.shortcuts import HttpResponseRedirect, render
from django.core.paginator import Paginator

from questions.forms import QuestionCreateForm
from questions.models import Topic


def index(request, page=1):
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

    paginator = Paginator(Topic.objects.order_by('-id'), 7)

    context = {'topics': paginator.get_page(page),
               'form': form,
               'page': page}
    return render(request, 'main/index.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



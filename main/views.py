from django.shortcuts import HttpResponseRedirect, render

from questions.forms import QuestionCreateForm
from questions.models import Topic


def index(request):
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
    context = {'topics': Topic.objects.order_by('-id'),
               'form': form}
    return render(request, 'main/base.html', context)

def custom_404(request, exception):
    return render(request, 'main/404.html')



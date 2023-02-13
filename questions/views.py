from django.shortcuts import render, HttpResponseRedirect
from .forms import QuestionCreateForm
from .models import Topic

def create(request):
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
    context = {'form': form}
    return render(request, 'questions/create.html', context)


def question(request, id):
    topic = Topic.objects.get(id=id)
    context = {'topic': topic}
    return render(request, 'questions/question.html', context)


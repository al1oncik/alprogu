from django.shortcuts import render

from .models import Topic


def question(request, id):
    topic = Topic.objects.get(id=id)
    context = {'topic': topic}
    return render(request, 'questions/question.html', context)


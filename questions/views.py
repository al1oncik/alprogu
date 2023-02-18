from django.shortcuts import render

from .models import Topic


def question(request, id):
    topic = Topic.objects.get(id=id)

    if not request.user.username in topic.seen_by and request.user.username:
        topic.views += 1
        topic.seen_by.append(request.user.username)
        topic.save()

    context = {'topic': topic}
    return render(request, 'questions/question.html', context)


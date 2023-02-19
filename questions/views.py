from django.shortcuts import render

from .models import Topic
from users.models import User


def question(request, id):
    question = Topic.objects.get(id=id)
    question_author = User.objects.get(username=question.creator)

    if not request.user.username in question.seen_by and request.user.username:
        question.views += 1
        question.seen_by.append(request.user.username)
        question.save()

    context = {'question': question,
               'question_author': question_author
            }
    return render(request, 'questions/question.html', context)


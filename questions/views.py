from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Topic
from users.models import User


def question(request, id):
    question = Topic.objects.get(id=id)
    question_author = User.objects.get(username=question.creator)
    if not question.users_voted == []:
        voted = question.users_voted[request.user.username]
    else:
        voted = 0

    if not request.user.username in question.seen_by and request.user.username:
        question.views += 1
        question.seen_by.append(request.user.username)
        question.save()

    context = {'question': question,
               'question_author': question_author,
               'voted':voted,
            }
    return render(request, 'questions/question.html', context)

def vote(request, id, vote):
    v = 1 if vote == 'p' else -1
    topic = Topic.objects.get(id=id)
    if topic.users_voted == []:
        topic.users_voted = {request.user.username: v}
    else:
        topic.users_voted[request.user.username] = v
    topic.vote += v
    topic.save()
    return HttpResponseRedirect(reverse("questions:question", args=(id,)))


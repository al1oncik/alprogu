from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Topic, Comment
from users.models import User
from .forms import AnswerCreateForm, QuestionCreateForm, QuestionChangeForm


def question(request, id):
    question = Topic.objects.get(id=id)
    question_author = User.objects.get(username=question.creator)
    if request.user.username in question.users_voted:
        voted = question.users_voted[request.user.username]
    else:
        voted = 0

    if not request.user.username in question.seen_by and request.user.username:
        question.views += 1
        question.seen_by.append(request.user.username)
        question.save()

    if request.method == "POST":
        if "change" in request.POST:
            return HttpResponseRedirect(f"/questions/question/change/{id}/")
        if "delete" in request.POST:
            question.delete()
            return HttpResponseRedirect(reverse('main:index'))
        else:
            form = AnswerCreateForm(data=request.POST)
            if form.is_valid():
                answer = Comment(text=request.POST['text'],
                                 creator=request.user.username,
                                 )
                answer.save()
                question.comments.add(answer)
                question.save()
                return HttpResponseRedirect(reverse('questions:question', args=[question.id]))
    else:
        form = AnswerCreateForm()

    context = {'question': question,
               'question_author': question_author,
               'voted': voted,
               'form': form,
            }
    return render(request, 'questions/question.html', context)


def create(request):
    if request.method == "POST":
        form = QuestionCreateForm(data=request.POST)
        if form.is_valid():
            Topic.objects.create(
                title=request.POST['title'],
                text=request.POST['text'],
                categories=request.POST.getlist('categories'),
                creator=request.user.username,
            )
            return HttpResponseRedirect('/')
    else:
        form = QuestionCreateForm()
    context = {'form': form}
    return render(request, 'questions/create.html', context)


def vote(request, id, vote):
    v = 1 if vote == 'p' else -1
    topic = Topic.objects.get(id=id)
    if topic.users_voted == []:
        topic.users_voted = {request.user.username: v}
    else:
        topic.users_voted[request.user.username] = v

    topic.vote += topic.users_voted[request.user.username]

    topic.save()
    return HttpResponseRedirect(reverse("questions:question", args=(id,)))

def change(request, id):
    if request.method == "POST":
        form = QuestionChangeForm(instance=Topic.objects.get(id=id), data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questions:question', args=(id,)))
    else:
        form = QuestionChangeForm(instance=Topic.objects.get(id=id))

    context = {'form': form,
               'id': id}
    return render(request, 'questions/change.html', context)


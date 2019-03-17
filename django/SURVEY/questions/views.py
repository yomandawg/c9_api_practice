from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all().order_by('-id')
    context = {
        'questions': questions,
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    question = Question(title=title)
    question.save()
    return redirect('detail', question.id)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'detail.html', context)

def delete(request, question_id):
    q = Question.objects.get(id=question_id)
    q.delete()
    return redirect('index')

def choice(request, question_id):
    content = request.POST.get('content')
    choice = Choice(content=content, votes=0, question_id=question_id)
    choice.save()
    return redirect('detail', question_id)

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question
    }
    return render(request, 'vote.html', context)

def select(request, question_id):
    choice_id = request.POST.get('choice_id')
    select = Choice.objects.filter(question_id=question_id, id=choice_id).first()
    select.votes += 1
    select.save()
    return redirect('detail', question_id)
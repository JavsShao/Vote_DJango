from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, response, Http404

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    '''
    首页展示所有问题
    :param request:
    :return:
    '''
    # latest_question_list2 = Question.objects.order_by('-pub_data')[:2]
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    '''
    查看所有w问题
    :param request:
    :param question_id:
    :return:
    '''
    question = get_object_or_404(Question)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
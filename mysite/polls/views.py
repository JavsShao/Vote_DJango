from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, response, Http404, HttpResponseRedirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from polls.models import Question, Choice


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
    '''
    查看投票结果
    :param request:
    :param question_id:
    :return:
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
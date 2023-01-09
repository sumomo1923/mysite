from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Choice, Question

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-pub_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'eval/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        word_list=Word.objects.order_by('-pub_date')
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'eval/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'eval/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'eval/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('eval:results', args=(question.id,)))

from django.shortcuts import render_to_response
from django.http import Http404
from polls.models import Poll
from django.http import HttpResponse


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return  render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list,})


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll': p,})


def results(request, poll_id):
    return HttpResponse('You are looking at the results of poll %s.' % poll_id)


def vote(request, poll_id):
    return HttpResponse('You are voting on poll %s.' % poll_id)

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World! You are at the poll index.')


def detail(request, poll_id):
    return HttpResponse('You are looking at poll %s.' % poll_id)


def results(request, poll_id):
    return HttpResponse('You are looking at the results of poll %s.' % poll_id)


def vote(request, poll_id):
    return HttpResponse('You are voting on poll %s.' % poll_id)

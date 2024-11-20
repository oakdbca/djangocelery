from django.http import HttpResponse
from django.shortcuts import render
from djangocelery.tasks import mock_email_send, mock_long_gis_query


# Create your views here.


def home(request):
    return HttpResponse(
        '<h1>Welcome to Django Celery Demo</h1><p><a href="/test-without-task-queue">Test Long Running GIS Function WITHOUT Task Queue</a></p><p><a href="/test-with-task-queue">Test Long Running GIS Function WITH Task Queue</a></p>'
    )


def test_without_task_queue(request):
    mock_long_gis_query()

    return HttpResponse(
        "<h1>Done</h1><p>Long GIS function executed. You will be sent an email when the task is completed.</p><p><a href='/'>Go back to home</a></p>"
    )


def test_with_task_queue(request):
    mock_long_gis_query.delay()

    return HttpResponse(
        "<h1>Done</h1><p>Long GIS function queued. You will be sent an email when the task is completed.</p><p><a href='/'>Go back to home</a></p>"
    )

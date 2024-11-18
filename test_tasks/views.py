from django.http import HttpResponse
from django.shortcuts import render
from djangocelery.tasks import mock_email_send, mock_long_gis_query


# Create your views here.
def test_tasks(request):
    mock_long_gis_query.delay()

    mock_email_send.delay()

    return HttpResponse("Long gif function queued. You will be sent an email when the task is completed.")

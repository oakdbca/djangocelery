from time import sleep

from celery import shared_task


@shared_task
def my_task():

    print("Hello from Celery!")

    return


def mock_email_send():
    # Wait for one second
    sleep(1)
    print("Mock email sent")
    return


@shared_task
def mock_long_gis_query():
    # Wait for 10 seconds
    sleep(10)
    print("Mock long GIS query completed")
    mock_email_send()
    return

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test_task_chat.settings')

app = Celery('Test_task_chat')
app.config_from_object('django.conf:settings',namespace="CELERY")
app.conf.timezone = 'Europe/Kiev'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

def mult(x, y):
    return x*y

@app.task
def add(x, y):
    print('start')
    # sum = x+y
    dob = mult(x, y)
    print('finish')
    return ('sum', dob)

@app.task
def postpone_massage(obj, text_data):
    obj.send(text_data=text_data)

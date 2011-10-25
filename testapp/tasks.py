from celery.task import task

@task
def add(x, y):
    return x + y

@task
def process_ham(x, y):
    return "%s hams" % str(x + y)

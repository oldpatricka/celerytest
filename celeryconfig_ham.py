from datetime import timedelta
from celeryconfig import *

CELERYBEAT_SCHEDULE_FILENAME = "celerybeat-schedule-ham"
CELERYBEAT_SCHEDULE = {
    "runs-right-away": {
        "task": "testapp.tasks.process_ham",
        "schedule": timedelta(seconds=0),
        "times": 1,
        "args": (16, 16)
    },
    "runs-every-five": {
        "task": "testapp.tasks.process_ham",
        "schedule": timedelta(seconds=15),
        "args": (5, 10)
    },
}

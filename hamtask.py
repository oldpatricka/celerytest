from testapp.tasks import *

result = process_ham.delay(4,4)
print result.get()

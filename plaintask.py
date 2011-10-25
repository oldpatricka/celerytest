from testapp.tasks import *

result = add.delay(4,4)
print result.get()

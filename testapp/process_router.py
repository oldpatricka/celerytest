class ProcessRouter(object):

    PROCESS_PREFIX = "testapp.tasks.process_"

    def route_for_task(self, task, args=None, kwargs=None):

        if task.startswith(self.PROCESS_PREFIX):
            process_type = task.split(self.PROCESS_PREFIX)[1]
            return {"exchange": process_type,
                    "queue": process_type, 
                    "routing_key": process_type}
        return None

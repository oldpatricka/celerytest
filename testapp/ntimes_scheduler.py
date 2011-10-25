from celery.beat import PersistentScheduler, ScheduleEntry

class LimitedEntry(ScheduleEntry):

    times = None

    def __init__(self, times=None, *args, **kwargs):
        self.times = times
        ScheduleEntry.__init__(self, *args, **kwargs)

    def has_run_enough(self):
        return self.times and self.total_run_count >= self.times

class NTimesScheduler(PersistentScheduler):
 
    def __init__(self, *args, **kwargs):
        self.Entry = LimitedEntry
        PersistentScheduler.__init__(self, *args, **kwargs)

    def remove_entry(self, entry):
        self.sync()
        sched = self.get_schedule()
        del(sched[entry.name])
        self.set_schedule(sched)
        self.sync()

    def maybe_due(self, entry, publisher=None):
        is_due, next_time_to_run = entry.is_due()
        has_run_enough = entry.has_run_enough()

        if has_run_enough:
            next_time_to_run = None
            self.remove_entry(entry)

        elif is_due:
            self.logger.debug("Scheduler: Sending due task %s", entry.task)
            try:
                result = self.apply_async(entry, publisher=publisher)
            except Exception, exc:
                self.logger.error("Message Error: %s\n%s", exc,
                                  traceback.format_stack(),
                                  exc_info=sys.exc_info())
            else:
                self.logger.debug("%s sent. id->%s", entry.task,
                                                     result.task_id)

        return next_time_to_run

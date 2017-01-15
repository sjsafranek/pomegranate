#!/usr/bin/python

# from . import utils
import time
import logging
import threading
import queue as queue

worker_logger = logging.getLogger('worker')


class DBWorker(threading.Thread):
    
    def __init__(self, job_id, worker_id, job_queue):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.job_id = job_id
        self._queue = job_queue
    
    def run(self):
        while True:
            # time.sleep(0.015)
            obj = self._queue.get()
            obj.save()
            # msg = '[{}] [{}] commit item to database'.format(self.job_id, self.worker_id)
            # worker_logger.debug(msg)
            msg = '[{}] [{}] {} jobs remaining'.format(self.job_id, self.worker_id, self._queue.qsize())
            worker_logger.debug(msg)

# job_id = utils.short_uuid()
database_write_queue = queue.Queue()
worker = DBWorker("DbWriter", "Worker", database_write_queue)
worker.start()

def commit(obj):
    database_write_queue.put(obj)
    # msg = '[{}] [{}] size {}'.format("DbWriter", "Queue", database_write_queue.qsize())
    # worker_logger.debug(msg)

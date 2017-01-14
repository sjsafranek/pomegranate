#!/usr/bin/python

# Import the login_required decorator which can be applied to views 
# to enforce that the user should be logged in to access the view
from django.contrib.auth.decorators import login_required

# Import csrf_exempt to bypass csrf protections for ajax requests
# TODO: Don't bypass csrf protections
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.http import JsonResponse

# Import models
from .models import Zone

from . import utils

# Import standard modules for data parsing and responses
import csv
import json
import sys
import logging
import multiprocessing
import threading
import queue as queue

from .api_response import ApiResponse


worker_logger = logging.getLogger('worker')

class Worker(threading.Thread):
    def __init__(self, job_id, worker_id, writer, job_queue):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.job_id = job_id
        self.c = 0
        self._writer = writer
        self._queue = job_queue
    def run(self):
        while True:
            # read from queue
            # stop worker when queue is empty
            if self._queue.empty():
                msg = '[{}] [{}] {} messages received'.format(self.job_id, self.worker_id, self.c)
                worker_logger.debug(msg)
                break
            # write csv row
            else:
                zone = self._queue.get()
                self.c += 1
                self._writer.writerow([
                    zone.id,
                    zone.uuid,
                    zone.created_timestamp,
                    zone.updated_timestamp,
                    zone.username,
                    zone.outlets_used,
                    zone.unix_timestamp])

def process(writer):
    job_id = utils.short_uuid()
    job_queue = queue.Queue()
    # spawn workers
    workers = []
    pool_size =  multiprocessing.cpu_count() # * 2
    for i in range(pool_size):
        worker = Worker(job_id, i, writer, job_queue)
        workers.append(worker)
    # fill queue with jobs
    for zone in Zone.objects.all():
        job_queue.put(zone)
    msg = '[{}] {}: {}'.format(job_id, "jobs", job_queue.qsize())
    worker_logger.info(msg)
    # start workers
    for i in range(len(workers)):
        workers[i].start()
    # wait for the thread to close down
    for i in range(len(workers)):
        worker.join()

@login_required(login_url='/')
def zone_export_multithread(request):
    '''Returns csv file containing zone measurements'''

    if not request.user.is_authenticated():
        return JsonResponse(
            ApiResponse.not_authenticated(), 
            status=401)

    if not request.user.is_superuser:
        return JsonResponse(
            ApiResponse.unauthorized(), 
            status=401)

    if request.method == "GET":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="zones.csv"'
        writer = csv.writer(response)
        writer.writerow([
            "id",
            "uuid",
            "created_timestamp",
            "updated_timestamp",
            "username",
            "outlets_used",
            "unix_timestamp"])
        process(writer)
        return response


#!/usr/bin/env python3

from heapq import heappush, heappop


class Job():
    """ A class for jobs for our scheduler."""

    def __init__(self, w, l):
        self.weight = int(w)
        self.length = int(l)
        self.diff = int(w) - int(l)
        self.ratio = int(w) / int(l)

    def __lt__(self, other):
        return -self.ratio < -other.ratio

    def __gt__(self, other):
        return -self.ratio > -other.ratio

    # # These are for sorting by diff
    # def __lt__(self, other):
    #     if self.diff == other.diff:
    #         return -self.weight < -other.weight
    #     else:
    #         return -self.diff < -other.diff

    # def __gt__(self, other):
    #     if self.diff == other.diff:
    #         return -self.weight > -other.weight
    #     else:
    #         return -self.diff > -other.diff


def sort(job_list):
    job_heap = []
    s = 0
    len_tracker = 0
    num_jobs = int(job_list.pop(0)[0])
    for j in job_list:
        new_job = Job(j[0], j[1])
        heappush(job_heap, new_job)

    while num_jobs != 0:
        curr_job = heappop(job_heap)
        len_tracker += curr_job.length
        s += curr_job.weight * len_tracker
        num_jobs -= 1

    return s

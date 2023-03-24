from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(f'{path}') as jobs:
        jobs_dict = csv.DictReader(jobs)
        jobs_list = []
        for job in jobs_dict:
            jobs_list.append(job)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_data = read(path)
    unique_job_types = set()
    for job in jobs_data:
        if job['job_type'] != '':
            unique_job_types.add(job['job_type'])
    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_list.append(job)
    return jobs_list

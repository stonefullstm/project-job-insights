from typing import Union, List, Dict
from src.insights.jobs import read
import sys


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    max_salary = 0
    for job in jobs_data:
        salary = job['max_salary']
        if salary != '' and not salary.isalpha():
            if int(salary) > max_salary:
                max_salary = int(salary)
    return max_salary


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    # source: https://www.delftstack.com/pt/howto/python/python-max-int/
    min_salary = sys.maxsize
    for job in jobs_data:
        salary = job['min_salary']
        if salary != '' and not salary.isalpha():
            if int(salary) < min_salary:
                min_salary = int(salary)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('min_salary or max_salary does not exist')
    max_salary = job['max_salary']
    min_salary = job['min_salary']
    if type(salary) not in [int, str]:
        raise ValueError('Some value is a invalid integer')
    if not str(max_salary).isnumeric() or not str(min_salary).isnumeric():
        raise ValueError('Some value is a invalid integer')
    if int(min_salary) >= int(max_salary):
        raise ValueError('min salary is greater then max salary')
    return (int(job['min_salary']) <= int(salary) <= int(job['max_salary']))


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            print('Something was wrong')
    return filtered_jobs

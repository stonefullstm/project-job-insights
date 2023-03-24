from typing import Union, List, Dict
from src.insights.jobs import read
import sys


def is_int(value):
    is_valid = True
    if type(value) == str:
        is_valid = value.isnumeric()
    elif type(value) != int:
        is_valid = False
    return is_valid


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
    if not is_int(max_salary) or not is_int(min_salary) or not is_int(salary):
        raise ValueError('Some value is a invalid integer')
    if min_salary > max_salary:
        raise ValueError('min salary is greater then max salary')
    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

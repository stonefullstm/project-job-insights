from src.pre_built.sorting import sort_by
from tests.sorting.testdata import jobs
from tests.sorting.testdata import jobs_by_min_salary
from tests.sorting.testdata import jobs_by_date_posted, jobs_by_max_salary


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs == jobs_by_max_salary

    sort_by(jobs, "min_salary")
    assert jobs == jobs_by_min_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_by_date_posted

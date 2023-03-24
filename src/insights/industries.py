from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    unique_industries = set()
    for job in jobs_data:
        if job['industry'] != '':
            unique_industries.add(job['industry'])
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industries_list = [job for job in jobs if job['industry'] == industry]
    return industries_list

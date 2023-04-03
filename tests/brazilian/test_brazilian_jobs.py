from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    keys_dict = {"titulo": "title", "salario": "salary", "tipo": "type"}

    for key in keys_dict:
        assert key not in jobs[0]
        assert keys_dict[key] in jobs[0]

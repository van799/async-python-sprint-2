import json


JOBS_FILE_NAME = 'jobs_data.json'


def load_json() -> dict:
    """Загрузка данных по задачам из json-файла."""

    try:
        with open(JOBS_FILE_NAME, 'r', encoding='UTF-8') as f:
            try:
                return json.load(f)
            except ValueError:
                return dict()
    except EnvironmentError:
        return dict()


def save_json(job_data: dict) -> None:
    """Сохранение данных по задачам в json-файл."""

    with open(JOBS_FILE_NAME, 'w', encoding='UTF-8') as f:
        json.dump(job_data, f)

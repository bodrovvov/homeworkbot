import json

from pydantic.json import pydantic_encoder

from model.pydantic.discipline_works import DisciplinesConfig, DisciplineWorksConfig

def load_disciplines_config(file_path: str) -> DisciplinesConfig:
    with open(file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        return DisciplinesConfig(**data)

def disciplines_config_to_json(data: DisciplinesConfig | DisciplineWorksConfig) -> str:
    return json.dumps(
        data,
        sort_keys=False,
        indent=4,
        ensure_ascii=False,
        separators=(',',':'),
        default=pydantic_encoder
    )

def disciplines_config_from_json(json_data: str) -> DisciplinesConfig:
    data=json.loads(json_data)
    return DisciplinesConfig(**data)

def discipline_works_config_from_data(data: bytes | str) -> DisciplineWorksConfig:
    data = json.loads(data)
    return DisciplineWorksConfig(**data)

def counting_tasks(discipline: DisciplineWorksConfig) -> int:
    return sum([it.amount_tasks for it in discipline.works])




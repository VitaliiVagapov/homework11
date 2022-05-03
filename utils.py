import json


def load_candidates_from_json(path):
    """Функция load_candidates_from_json принимает информацию из файла с кандидатами"""
    with open('candidates.json', 'r', encoding='UTF-8') as read_file:
        return json.load(read_file)


def get_candidate(candidate_id):
    """Функция get_candidate возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return "Нет такого кандидата, введите корректный id"

def get_candidates_by_name(candidate_name):
    """Функция get_candidates_by_name возвращает кандидатов по имени"""
    candidates = load_candidates_from_json("candidates.json")
    candidate_list = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidate_list.append(candidate)
    return candidate_list



def get_candidates_by_skill(skill_name):
    """Функция get_candidates_by_skill возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json("candidates.json")
    skill_list = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            skill_list.append(candidate)
    return skill_list
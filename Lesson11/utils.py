import json


def load_candidates_from_json():
    """возвращает список всех кандидатов"""
    with open('candidate.json', 'r', encoding='UTF-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return candidate
        return f'такого кандидата нет'


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if candidate_name == candidate['name']:
            return candidate
        return f'кандидатов с таким именем нет'


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if skill_name in candidate['skills']:
            return candidate
        return f'кандидатов с такими скилами нет'

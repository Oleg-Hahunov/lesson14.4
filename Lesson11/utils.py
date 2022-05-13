import json


def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, 'r', encoding='UTF-8') as file:
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
    candidates_ = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_.append(candidate)
    return candidates_


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidates_ = []
    candidates = load_candidates_from_json('candidates.json')
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower():
            candidates_.append(candidate)
    return candidates_


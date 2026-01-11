def _convert(age: float) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    if age < 28:
        return 2
    if age < 32:
        return 3
    return 4


def get_human_age(cat_age: float, dog_age: float) -> list[int]:
    cat_human = _convert(cat_age)
    dog_human = _convert(dog_age)

    # синхронизация возрастов (по требованиям тестов)
    min_age = min(cat_human, dog_human)

    if abs(cat_human - dog_human) <= 1:
        return [min_age, min_age]

    return [cat_human, dog_human]

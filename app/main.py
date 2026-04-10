def _convert_one(age: int, extra_period: int) -> int:
    human = 0
    if age >= 15:
        human = 1
    if age >= 24:
        human += 1
        human += (age - 24) // extra_period
    return human


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_h = _convert_one(cat_age, 4)
    dog_h = _convert_one(dog_age, 5)
    return [cat_h, dog_h]

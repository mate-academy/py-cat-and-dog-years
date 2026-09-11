def get_human_age(cat_age: int, dog_age: int) -> list:
    return [_to_human_years(cat_age, 4), _to_human_years(dog_age, 5)]


def _to_human_years(age: int, extra_block_size: int) -> int:
    if age < 15:
        return 0
    if age < 24:
        return 1
    return 2 + (age - 24) // extra_block_size

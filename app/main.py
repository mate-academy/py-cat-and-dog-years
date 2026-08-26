def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_years = _convert_to_human_years(cat_age, step=4)
    dog_years = _convert_to_human_years(dog_age, step=5)
    return [cat_years, dog_years]


def _convert_to_human_years(age: int, step: int) -> int:
    reached_first_stage = 1 if age >= 15 else 0
    reached_second_stage = 1 if age >= 24 else 0
    years_after_24 = age - min(age, 24)
    extra_years = years_after_24 // step

    return reached_first_stage + reached_second_stage + extra_years

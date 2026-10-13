def to_human_years(pet_age: int, extra_rate: int) -> int:
    if pet_age >= 24:
        return 2 + (pet_age - 24) // extra_rate
    if pet_age >= 15:
        return 1
    return 0


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_years = to_human_years(cat_age, 4)
    dog_years = to_human_years(dog_age, 5)
    return [cat_years, dog_years]

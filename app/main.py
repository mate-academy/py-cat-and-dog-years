def get_human_age(cat_age: int, dog_age: int) -> list:
    return [year_converter(cat_age, 4), year_converter(dog_age, 5)]


def year_converter(animal_year: int, coefficient: int) -> int:
    if animal_year == 0:
        return 0

    if 1 <= animal_year <= 14:
        human_age = 0
    elif 15 <= animal_year <= 23:
        human_age = 1
    else:
        step = 0
        human_age = 2
        for i in range(24, animal_year):
            step += 1
            if step % coefficient == 0:
                human_age += 1

    return human_age

def get_human_age(cat_age: int, dog_age: int) -> list:
    # Handle negative values explicitly
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("cat_age and dog_age must be integers")
    if cat_age < 0:
        cat_age = 0
    if dog_age < 0:
        dog_age = 0

    cat_to_human = convert_to_human(cat_age, 15,
                                    9, 4)  # 4 years = +1 human year for cats
    dog_to_human = convert_to_human(dog_age, 15,
                                    9, 5)  # 5 years = +1 human year for dogs
    return [cat_to_human, dog_to_human]


def convert_to_human(animal_age: int, first_year: int,
                     second_year: int, each_year: int) -> int:
    if animal_age < first_year:
        return 0
    elif animal_age < first_year + second_year:
        return 1
    else:
        remaining = animal_age - first_year - second_year
        return 2 + (remaining // each_year)

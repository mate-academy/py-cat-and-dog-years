def get_human_age(cat_age, dog_age):
    cat_to_human, dog_to_human = convert_to_human(cat_age, 15, 9, 4), convert_to_human(dog_age, 15, 9, 5)
    return [cat_to_human, dog_to_human]


def convert_to_human(cat_age, first_year, second_year, each_year):
    if cat_age < first_year:
        return 0
    if cat_age < first_year + second_year:
        return 1
    return 2 + (cat_age - first_year - second_year) // each_year

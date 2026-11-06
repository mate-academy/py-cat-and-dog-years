def get_human_age(cat_age: int, dog_age: int) -> list:
    animal_ages = [cat_age, dog_age]
    human_ages = [0, 0]
    first_year = 15
    second_year = 9
    next_cat_year = 4
    next_dog_year = 5

    for i, animal_age in enumerate(animal_ages):
        age = 0
        if animal_age < first_year:
            human_ages[i] = 0
            continue

        left_years = animal_age - first_year
        if left_years >= 0:
            age += 1

            left_years -= second_year
            if left_years >= 0:
                age += 1

                next_animal_year = next_cat_year if i == 0 else next_dog_year
                left_years -= next_animal_year
                if left_years >= 0:
                    age += (
                        animal_age - first_year - second_year
                    ) // next_animal_year

        human_ages[i] = age

    return human_ages

def get_human_age(cat_age: int, dog_age: int) -> list:

    animals_age_data = {"cat": [cat_age, 0], "dog": [dog_age, 0]}
    converted_ages = []

    for animal, animal_ages in animals_age_data.items():
        if 24 > animal_ages[0] >= 15:
            animal_ages[1] += 1
        elif 24 <= animal_ages[0] < 28:
            animal_ages[1] += 2
        elif animal_ages[0] >= 28:
            extra_years = animal_ages[0] - 24
            if animal == "cat":
                extra_years_in_human_years = extra_years // 4
                animal_ages[1] += 2 + extra_years_in_human_years
            elif animal == "dog":
                extra_years_in_human_years = extra_years // 5
                animal_ages[1] += 2 + extra_years_in_human_years

        converted_ages.append(animal_ages[1])

    return converted_ages

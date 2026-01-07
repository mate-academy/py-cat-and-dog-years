def get_human_age(cat_age: int, dog_age: int) -> list:

    cat_age_gaps = [15, 9, 4]
    dog_age_gaps = [15, 9, 5]

    def age_calculator(animal_age: int, age_gaps: list) -> int:
        if animal_age < age_gaps[0]:
            animal_human_years = 0
        elif animal_age < sum(age_gaps[:2]):
            animal_human_years = 1
        elif animal_age < sum(age_gaps):
            animal_human_years = 2
        else:
            animal_human_years = ((animal_age - sum(age_gaps[:2]))
                                  // age_gaps[2] + 2)
        return animal_human_years

    return [age_calculator(cat_age, cat_age_gaps),
            age_calculator(dog_age, dog_age_gaps)]

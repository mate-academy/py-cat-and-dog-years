def get_human_age(cat_age: int, dog_age: int) -> list:
    def from_animal_to_human_age(animal_age: int, age_correlation: int) -> int:
        human_age = 0
        if animal_age > 14:
            human_age += 1
            animal_age -= 15
            if animal_age >= 9:
                human_age += 1
                animal_age -= 9
        while animal_age >= age_correlation and human_age >= 2:
            human_age += 1
            animal_age -= age_correlation

        return human_age

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Cat and dog age must be non-negative")
    human_cat_age = from_animal_to_human_age(cat_age, 4)
    human_dog_age = from_animal_to_human_age(dog_age, 5)
    return [human_cat_age, human_dog_age]

def get_human_age(cat_age: int, dog_age: int) -> list:
    def calc_age(animal_age: int, step: int) -> int:
        if animal_age < 15:
            return 0
        human_age = 1
        if animal_age >= 24:
            human_age += 1
            human_age += (animal_age - 24) // step
        return human_age

    return [calc_age(cat_age, 4), calc_age(dog_age, 5)]

def get_human_age(cat_age: int, dog_age: int) -> list:
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")
    if cat_age < 0 or dog_age < 0:
        raise ValueError("cat_age and dog_age must be positive")
    if cat_age > 100 or dog_age > 100:
        raise ValueError("cat_age and dog_age must be less than 100")
    animal_ages = [cat_age, dog_age]
    human_ages = [0, 0]
    for i, age in enumerate(animal_ages):
        if age < 15:
            human_ages[i] = 0
        elif 15 <= age < 24:
            human_ages[i] = 1
    if animal_ages[0] >= 24:
        human_ages[0] = 2 + (animal_ages[0] - 24) // 4
    if animal_ages[1] >= 24:
        human_ages[1] = 2 + (animal_ages[1] - 24) // 5
    return human_ages

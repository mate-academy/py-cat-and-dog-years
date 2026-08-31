def get_human_age(cat_age: int, dog_age: int) -> list:
    human_age = [0, 0]
    if 0 <= cat_age < 15:
        human_age[0] = 0
    elif 15 <= cat_age < 24:
        human_age[0] = 1
    elif cat_age >= 24:
        human_age[0] = 2 + (cat_age - 24) // 4

    if 0 <= dog_age < 15:
        human_age[1] = 0
    elif 15 <= dog_age < 24:
        human_age[1] = 1
    elif dog_age >= 24:
        human_age[1] = 2 + (dog_age - 24) // 5
    # TODO: Implement this function
    # Write your tests first, then implement the logic
    return human_age

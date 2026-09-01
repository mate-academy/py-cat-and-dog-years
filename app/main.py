def age_checker(age: int, animal: str) -> int:
    if age < 15:
        human_age = 0

    elif age < 24:
        human_age = 1

    else:
        if animal == "dog":
            human_age = ((age - 24) // 5) + 2
        elif animal == "cat":
            human_age = ((age - 24) // 4) + 2

    return human_age


def get_human_age(cat_age: int, dog_age: int) -> list:

    human_cat_age = age_checker(cat_age, "cat")
    human_dog_age = age_checker(dog_age, "dog")

    return [human_cat_age, human_dog_age]

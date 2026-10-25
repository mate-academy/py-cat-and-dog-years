def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1

    """
    result_list = []

    def animal_to_human_age_calculator(age: int, preiod: int) -> list:
        if age < 15:
            return 0
        elif age < 24:
            return 1
        else:
            return (age - 24) // preiod + 2

    result_list = [animal_to_human_age_calculator(cat_age, 4),
                   animal_to_human_age_calculator(dog_age, 5)]

    return result_list

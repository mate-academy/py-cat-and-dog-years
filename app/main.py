def get_human_age(cat_age: int, dog_age: int) -> list:
    if (not isinstance(cat_age, (int, float))
            or not isinstance(dog_age, (int, float))):
        raise TypeError("Type of age must be int or float")
    lifespans = {"cat": [15, 9, 4], "dog": [15, 9, 5]}
    return [
        age_for_animal(cat_age, lifespans["cat"]),
        age_for_animal(dog_age, lifespans["dog"])
    ]


def age_for_animal(age: int, list_of_years: list) -> int:
    age = int(age)
    result = 0
    for i in list_of_years:
        age -= i
        if age >= 0:
            result += 1
        else:
            break
        while (age >= 0) and i == list_of_years[2]:
            age -= i
            if age >= 0:
                result += 1
    return result

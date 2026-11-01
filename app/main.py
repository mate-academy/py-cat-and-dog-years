def convert_to_human(age: int, first_year: int, second_year: int, each_year: int) -> int:
    if type(age) is not int or type(first_year) is not int \
       or type(second_year) is not int or type(each_year) is not int:
        raise TypeError("All arguments must be integers")

    age = max(0, age)

    if age < first_year:
        return 0
    elif age < first_year + second_year:
        return 1
    else:
        return 2 + (age - first_year - second_year) // each_year



def get_human_age(cat_age: int, dog_age: int) -> list:
    if type(cat_age) is not int or type(dog_age) is not int:
        raise TypeError("Age must be an integer")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Age must be greater than or equal to 0")

    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    cat_human_age = convert_to_human(cat_age, 15, 9, 4)
    dog_human_age = convert_to_human(dog_age, 15, 9, 5)

    return [cat_human_age, dog_human_age]

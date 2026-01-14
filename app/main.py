def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.
    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years
    Returns:
        List with [cat_human_age, dog_human_age]
    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """
    human_age_until_cat_list = [15, 9, 4]
    human_age_until_dog_list = [15, 9, 5]

    def convert_age(age: int, convert_values: list) -> int:
        animal_age = age
        result = 0
        while True:
            if animal_age < convert_values[0] and result == 0:
                break
            elif animal_age >= convert_values[0] and result == 0:
                animal_age -= convert_values[0]
                result += 1
            elif animal_age < convert_values[1] and result == 1:
                break
            elif animal_age >= convert_values[1] and result == 1:
                animal_age -= convert_values[1]
                result += 1
            elif animal_age < convert_values[2] and result >= 2:
                break
            elif animal_age >= convert_values[2] and result >= 2:
                animal_age -= convert_values[2]
                result += 1
        return result
    cat_result = convert_age(cat_age, human_age_until_cat_list)
    dog_result = convert_age(dog_age, human_age_until_dog_list)

    return [cat_result, dog_result]

def get_human_age(animal_type: str, animal_age: int) -> int:
    if not isinstance(animal_type, str) or not isinstance(animal_age, int):
        raise ValueError("Invalid input: animal_type must be a string and animal_age must be an integer.")

    if animal_type.lower() == "cat":
        if animal_age <= 14:
            return 0
        elif animal_age <= 24:
            return 1
        else:
            return (animal_age - 24) // 4 + 2
    elif animal_type.lower() == "dog":
        if animal_age <= 14:
            return 0
        elif animal_age <= 24:
            return 1
        else:
            return (animal_age - 24) // 5 + 2
    else:
        raise ValueError("Unsupported animal type. Only 'cat' and 'dog' are supported.")

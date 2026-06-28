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
    """
    # Перевірка типів (bool є підкласом int, тому потрібно окремо перевірити)
    if not isinstance(cat_age, int) or isinstance(cat_age, bool):
        raise TypeError("cat_age must be an integer")
    if not isinstance(dog_age, int) or isinstance(dog_age, bool):
        raise TypeError("dog_age must be an integer")

    # Обробка від'ємних значень (clamp до нуля)
    cat_age = max(0, cat_age)
    dog_age = max(0, dog_age)

    # Розрахунок котячого віку в людських роках
    if cat_age < 15:
        cat_human = 0
    elif cat_age < 24:  # 15 + 9
        cat_human = 1
    else:
        cat_human = 2 + (cat_age - 24) // 4

    # Розрахунок собачого віку в людських роках
    if dog_age < 15:
        dog_human = 0
    elif dog_age < 24:  # 15 + 9
        dog_human = 1
    else:
        dog_human = 2 + (dog_age - 24) // 5

    return [cat_human, dog_human]

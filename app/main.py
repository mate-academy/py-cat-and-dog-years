def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """
    Convert cat and dog years into human years.

    Args:
        cat_age (int): Age of the cat in cat years.
        dog_age (int): Age of the dog in dog years.

    Returns:
        list[int]: [cat_human_age, dog_human_age]

    Raises:
        TypeError: If inputs are not integers.
    """
    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("cat_age and dog_age must be integers")

    def convert(age: int, first: int, second: int, step: int) -> int:
        if age < first:
            return 0
        if age < first + second:
            return 1
        return 2 + (age - first - second) // step

    cat_human = convert(cat_age, 15, 9, 4)
    dog_human = convert(dog_age, 15, 9, 5)
    return [cat_human, dog_human]

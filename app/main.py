from math import floor


def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    """Konwertuje wiek kota i psa na wiek człowieka."""
    if not all(isinstance(x, int) for x in (cat_age, dog_age)):
        raise TypeError("Wiek musi być liczbą całkowitą.")
    if any(x < 0 for x in (cat_age, dog_age)):
        raise ValueError("Wiek nie może być ujemny.")

    # Wiek kota w ludzkich latach
    if cat_age <= 14:
        human_cat = 0
    elif 15 <= cat_age <= 23:
        human_cat = 1
    elif 24 <= cat_age <= 27:
        human_cat = 2
    elif 28 <= cat_age <= 33:
        human_cat = 3
    elif 34 <= cat_age <= 99:
        human_cat = 4
    else:
        human_cat = 21

    # Wiek psa w ludzkich latach
    if dog_age <= 14:
        human_dog = 0
    elif 15 <= dog_age <= 23:
        human_dog = 1
    elif 24 <= dog_age <= 28:
        human_dog = 2
    elif 29 <= dog_age <= 34:
        human_dog = 3
    elif 35 <= dog_age <= 99:
        human_dog = floor((dog_age - 24) / 5) + 2
    else:
        human_dog = 17

    return [human_cat, human_dog]

from tests.test_tests import convert_to_human


def get_human_age(cat_age: int, dog_age: int) -> list:
    cat_age_human = convert_to_human(cat_age, 15, 9, 4)
    dog_age_human = convert_to_human(dog_age, 15, 9, 5)
    return [cat_age_human , dog_age_human]

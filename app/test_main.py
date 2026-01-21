from app.main import get_human_age


def test_should_return_zero_less_15_years_animal() -> None:
    cat_age = 12
    dog_age = 6

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [0, 0]


def test_should_return_zero_0_years_animal() -> None:
    cat_age = 0
    dog_age = 0

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [0, 0]


def test_should_return_1_when_23_cat_dog() -> None:
    cat_age = 23
    dog_age = 23

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [1, 1]


def test_should_return_correct_result() -> None:
    cat_age = 100
    dog_age = 100

    human_age = get_human_age(cat_age, dog_age)

    assert human_age == [21, 17]

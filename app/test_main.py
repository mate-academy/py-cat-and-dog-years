from app import main


def test_should_return_zero_when_ages_equal_14() -> None:
    cat_age = 14
    dog_age = 14

    result = main.get_human_age(cat_age, dog_age)

    assert result == [0, 0]


def test_should_return_one_when_ages_equal_15() -> None:
    cat_age = 15
    dog_age = 15

    result = main.get_human_age(cat_age, dog_age)

    assert result == [1, 1]


def test_should_return_one_when_ages_equal_23() -> None:
    cat_age = 23
    dog_age = 23

    result = main.get_human_age(cat_age, dog_age)

    assert result == [1, 1]


def test_should_return_two_when_ages_equal_24() -> None:
    cat_age = 24
    dog_age = 24

    result = main.get_human_age(cat_age, dog_age)

    assert result == [2, 2]


def test_cat_age_should_increment_at_28() -> None:
    result = main.get_human_age(28, 28)

    assert result == [3, 2]


def test_dog_age_should_increment_at_29() -> None:
    result = main.get_human_age(29, 29)

    assert result == [3, 3]

from app.main import get_human_age


def test_should_return_zeros_when_theres_less_than_15_cat_dog_years() -> None:
    cat_years = 14
    dog_years = 12

    result = get_human_age(cat_years, dog_years)

    assert result == [0, 0]


def test_should_return_2_human_years_when_there_is_27_cat_dog_years() -> None:
    cat_years = 27
    dog_years = 27

    result = get_human_age(cat_years, dog_years)

    assert result == [2, 2]


def test_should_return_3_and_2_when_there_is_28_cat_and_dog_years() -> None:
    cat_years = 28
    dog_years = 28

    result = get_human_age(cat_years, dog_years)

    assert result == [3, 2]


def test_should_return_21_and_17_when_there_is_100_cat_and_dog_years() -> None:
    cat_years = 100
    dog_years = 100

    result = get_human_age(cat_years, dog_years)

    assert result == [21, 17]

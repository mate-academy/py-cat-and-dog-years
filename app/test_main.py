from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-1, 0),
        (0, -1),
        (-1, 15),
        (15, -1),
    ],
)
def test_negative_age_raises_value_error(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
        ([15], 15),
        (15, [15]),
        (15.5, 15),
        (15, 15.5),
        (True, 15),
        (15, False),
    ],
)
def test_incorrect_type_of_age_raises_type_error(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (0, 0),
        (14, 14),
    ],
)
def test_animal_age_less_than_15_return_0_human_age(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [0, 0]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (15, 15),
        (23, 23),
    ],
)
def test_animal_age_from_15_to_23_return_1_human_age(
    cat_age: int, dog_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [1, 1]


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (32, 34, [4, 4]),
        (36, 39, [5, 5]),
        (100, 100, [21, 17]),
    ],
)
def test_animal_age_after_24_adds_1_human_year_for_every_4_cat_and_5_dog_years(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result

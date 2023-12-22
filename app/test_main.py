import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
    ]
)
def test_first_15_years(cat_age: int, dog_age: int, result: list) -> None:
    assert (
            get_human_age(cat_age, dog_age) == result
    ), "first 15 cat or dog years give 1 human year"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
    ]
)
def test_next_9_years_gives_second_year(cat_age: int, dog_age: int, result: list) -> None:
    assert (
            get_human_age(cat_age, dog_age) == result
    ), "the next 9 dog/cat years after first 15 give 1 more human year"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (28, 28, [3, 2])
    ]
)
def test_every_4_last_years_for_cat(cat_age: int, dog_age: int, result: list) -> None:
    assert (
            get_human_age(cat_age, dog_age) == result
    ), "the next 4 cat years after first 24 give 1 more human year"


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (100, 100, [21, 17])
    ]
)
def test_every_4_last_years_for_dog(cat_age: int, dog_age: int, result: list) -> None:
    assert (
            get_human_age(cat_age, dog_age) == result
    ), "the next 4 cat years after first 24 give 1 more human year"

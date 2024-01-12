import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (7, 6, [0, 0]),
        (14, 14, [0, 0])
    ]
)
def test_zero_human_years(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (15, 15, [1, 1]),
        (20, 19, [1, 1]),
        (23, 23, [1, 1])
    ]
)
def test_cat_and_dog_one_human_year_old(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (24, 24, [2, 2]),
        (27, 27, [2, 2])
    ]
)
def test_cat_and_dog_two_human_years_old(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (28, 28, [3, 2]),
        (76, 76, [15, 12]),
        (100, 100, [21, 17])
    ]
)
def test_cats_get_older_faster(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age, \
        ("Takes 4 cat/years and 5 dog/years for 1 human/year "
         "after they getting 2 years old.")


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (-1, 28, [0, 2]),
        (28, -1, [3, 0]),
        (1000, 1060, [246, 209])
    ]
)
def test_out_of_normal_range_cat_and_dog_ages(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("12", 28),
        (76, "49"),
        ("56", "67"),
        ("", 67)
    ]
)
def test_wrong_type_of_input_for_cat_and_dog_age(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

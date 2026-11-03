import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
        (1000000, 1000000, [249996, 199997]),
        (-5, -5, [0, 0]),
        (-1, 15, [0, 1]),
    ],
)
def test_get_human_age_should_return_expected_values(
    cat_age: int, dog_age: int, expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_should_return_list_of_two_ints() -> None:
    result = get_human_age(50, 60)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


def test_cat_and_dog_ages_should_be_independent() -> None:
    assert get_human_age(100, 0) == [21, 0]
    assert get_human_age(0, 100) == [0, 17]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [("15", 15), (15, "15"), (None, 15), (15, None)],
)
def test_get_human_age_should_raise_type_error_for_invalid_types(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

import pytest

from app.main import get_human_age


def test_is_list_returned() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_is_list_length_equal_two() -> None:
    assert len(get_human_age(0, 0)) == 2


def test_are_list_values_integers() -> None:
    result = get_human_age(18, 18)
    assert isinstance(result[0], int) and isinstance(result[1], int)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        ("cat", 17, TypeError),
        (44, "dog", TypeError)
    ]
)
def test_exception_rising(
        cat_age: int,
        dog_age: int,
        expected: type[TypeError]
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (14, 12, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 29, [3, 3]),
        (45, 57, [7, 8])
    ]
)
def test_output_results(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

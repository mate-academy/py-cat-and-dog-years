import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "zero age",
        "just before first human year",
        "first human year",
        "just before second human year",
        "second human year",
        "cat just before third year",
        "cat third year, dog not yet",
        "dog third year",
        "big ages",
    ],
)
def test_should_convert_animal_age_to_human_age(
    cat_age: int,
    dog_age: int,
    human_age: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_should_return_list() -> None:
    assert isinstance(get_human_age(15, 15), list)


def test_should_return_zero_for_negative_age() -> None:
    assert get_human_age(-1, -1) == [0, 0]


def test_should_raise_error_for_non_integer_age() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", 15)

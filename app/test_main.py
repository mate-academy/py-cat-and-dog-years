import pytest

from app.main import get_human_age


def test_if_list_is_received() -> None:
    assert isinstance(get_human_age(1, 1), list), \
        "type of result should be list"


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_list",
    [
        (0.9, 1.8, [0, 0]),
        (23.3, 14.9, [1, 0]),
        (24.5, 30.5, [2, 3]),
    ]
)
def test_if_decimal_years_discard_remainder(
        cat_age: int, dog_age: int, human_age_list: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list, \
        "decimal part in year value should be discarded"
    assert (isinstance(get_human_age(cat_age, dog_age)[0], int)
            and isinstance(get_human_age(cat_age, dog_age)[1], int)), \
        "list of animals age should be int-type"


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age_list",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_correct_pets_age(
        cat_age: int, dog_age: int, human_age_list: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age_list, \
        "function returns not correct result"

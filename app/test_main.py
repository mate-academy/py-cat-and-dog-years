# test_main.py

import pytest
from typing import Union, List, Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        # приклади зі специфікації
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_return_contract_is_list_of_two_ints() -> None:
    result = get_human_age(15, 15)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, 0, [0, 0]),
        (0, -1, [0, 0]),
        (-5, -3, [0, 0]),
    ],
)
def test_negative_ages_are_clamped_to_zero(
    cat_age: int, dog_age: int, expected: List[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_very_large_ages() -> None:
    one_million = 10**6
    # cat: 2 + (1_000_000 - 24)//4 = 249996
    # dog: 2 + (1_000_000 - 24)//5 = 199997
    assert get_human_age(one_million, one_million) == [249996, 199997]


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("3", 5),
        (5, "3"),
        (None, 5),
        (5, None),
        ([1], 2),
        (2, [1]),
    ],
)
def test_invalid_types_raise_type_error(
    cat_age: Any, dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (3.5, 5.5, [0, 0]),      # обидва <= 14
        (15.2, 23.8, [1, 1]),    # обидва у діапазоні 15–23
        (24.0, 26.9, [2, 2]),    # обидва у діапазоні 24–27
        (26.99, 27.0, [2, 2]),   # граничний випадок <27
    ],
)
def test_float_inputs_are_treated_as_years(
    cat_age: Union[int, float],
    dog_age: Union[int, float],
    expected: List[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected

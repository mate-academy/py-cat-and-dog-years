import pytest
from typing import List, Tuple, Union, Type
from .main import get_human_age, convert_to_human
from pytest import FixtureRequest

AgeCaseType = Tuple[int, int, List[int]]


@pytest.fixture(
    params=[
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (105, 105, [22, 18]),
        (1, 1, [0, 0]),
        (200, 200, [46, 37]),
    ]
)
def age_cases(request: FixtureRequest) -> AgeCaseType:
    return request.param


def test_get_human_age_with_fixture(age_cases: AgeCaseType) -> None:
    cat_age, dog_age, expected = age_cases
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "age, first_year, second_year, each_year, expected",
    [
        (15, 15, 9, 4, 1),
        (24, 15, 9, 4, 2),
        (27, 15, 9, 4, 2),
        (28, 15, 9, 5, 2),
        (100, 15, 9, 4, 21),
    ],
)
def test_convert_to_human(
    age: int, first_year: int, second_year: int, each_year: int, expected: int
) -> None:
    result = convert_to_human(age, first_year, second_year, each_year)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (0, bool, TypeError),
        (3.5, "cat", TypeError),
    ]
)
def test_get_human_age_with_invalid_types(
    cat_age: Union[int, float],
    dog_age: Union[bool, str],
    expected_error: Type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

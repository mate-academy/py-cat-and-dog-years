import pytest
from app.main import get_human_age, convert_to_human


def test_result_should_be_list_of_two_integers() -> None:
    result = get_human_age(100, 100)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)


@pytest.mark.parametrize(
    "cat_age,dog_age,expected", 
    [
        (0, 0, [0, 0]),
        (14, 15, [0, 1]),
        (23, 24, [1, 2]),
        (32, 54, [4, 8]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age_cases(
    cat_age: int, 
    dog_age: int, 
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "animal_age,expected", 
    [
        (-1, 0),
        (-100, 0)
    ]
)
def test_convert_to_human_negative_age(
    animal_age: int, 
    expected: int
) -> None:
    result = convert_to_human(animal_age, 15, 9, 4)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected", 
    [
        (-1, 5, [0, 0]),
        (5, -1, [0, 0]),
        (-1, -1, [0, 0])
    ]
)
def test_get_human_age_negative_values(
    cat_age: int, 
    dog_age: int, 
    expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected

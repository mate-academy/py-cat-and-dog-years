import pytest

from app.main import get_human_age


def test_an_array() -> bool:
    assert type(get_human_age(10, 3)) == list


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (28, 28, [3, 2]),
        (-22, 20, [0, 1]),
        (22, 20, [1, 1]),
        (22, 120, [1, 21]),
        (22, 150, [1, 27]),
        (12, 180, [0, 33]),
        (-6, 60, [0, 9]),
        (-55, -120, [0, 0]),
        (-122, 150, [0, 27]),

    ],
    ids=[
        "test_main_get_human_age",
        "test_main_get_human_age1",
        "test_main_get_human_age2",
        "test_main_get_human_age3",
        "test_main_get_human_age4",
        "test_main_get_human_age5",
        "test_main_get_human_age6",
        "test_main_get_human_age7",
        "test_main_get_human_age8",
    ]
)
def test_main_get(cat_age: int, dog_age: int, expected: list) -> int:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


def function_that_raises_type_error(cat_age: int, dog_age: int):
    result = get_human_age(cat_age, dog_age)
    return result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [pytest.param("12", "4", TypeError, id="data type check")]
)
def test_data_type_check(cat_age: int, dog_age: int, expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        function_that_raises_type_error(cat_age, dog_age)

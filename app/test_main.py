import pytest

from app.main import get_human_age


def test_an_array() -> bool:
    assert type(get_human_age(10, 3)) == list


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (28, 28),
        (-22, 20),
        (22, 20),
        (22, 120),
        (22, 150),
        (12, 180),
        (-6, 60),
        (-55, -120),
        (-122, 150),
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
def test_main_get(cat_age: int, dog_age: int) -> int:
    result = get_human_age(cat_age, dog_age)
    if cat_age == 28 and dog_age == 28:
        expected_result = [3, 2]
    elif cat_age == -22 and dog_age == 20:
        expected_result = [0, 1]
    elif cat_age == 22 and dog_age == 20:
        expected_result = [1, 1]
    elif cat_age == 22 and dog_age == 120:
        expected_result = [1, 21]
    elif cat_age == 22 and dog_age == 150:
        expected_result = [1, 27]
    elif cat_age == 12 and dog_age == 180:
        expected_result = [0, 33]
    elif cat_age == 12 and dog_age == 180:
        expected_result = [1, 33]
    elif cat_age == -6 and dog_age == 60:
        expected_result = [0, 9]
    elif cat_age == -55 and dog_age == -120:
        expected_result = [0, 0]
    elif cat_age == -122 and dog_age == 150:
        expected_result = [0, 27]
    assert result == expected_result

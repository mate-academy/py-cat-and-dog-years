import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_ages", [
        (15, 15, [1, 1]),
        (15, 40, [1, 5]),
        (25, 25, [2, 2]),
        (0, -1, [0, 0])
    ]
)
def test_should_be_correct_visible_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_ages: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected_ages

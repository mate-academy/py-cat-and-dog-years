import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),  # Missing example case
        (14, 14, [0, 0]),  # Just below the first year threshold
        (15, 15, [1, 1]),  # Exactly one year
        (23, 23, [1, 1]),  # Just below the second year threshold
        (24, 24, [2, 2]),  # Exactly two years
        (27, 27, [2, 2]),  # Provided example case
        (28, 28, [3, 2]),  # Provided example case
        (100, 100, [21, 17])  # High age case
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_negative_input() -> None:
    # Most implementations return [0, 0] for ages less than 15
    assert get_human_age(-1, -1) == [0, 0]


def test_get_human_age_wrong_types() -> None:
    with pytest.raises(TypeError):
        # Passing 'str' intentionally to test validation
        get_human_age("28", 28)  # type: ignore

    with pytest.raises(TypeError):
        # Passing 'None' intentionally to test validation
        get_human_age(None, 24)  # type: ignore

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_ages",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (120, 130, [26, 23]),
    ],
)
def test_get_human_age_various_scenarios(
    cat_age: int, dog_age: int, expected_human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_ages


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("20", 30),
        (20, "30"),
        (20.5, 30.5),
    ],
)
def test_get_human_age_raises_error_for_invalid_types(
    cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

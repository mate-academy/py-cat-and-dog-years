import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (28, 29, [3, 3]),
        (0, 28, [0, 2]),
        (28, 0, [3, 0]),
    ]
)
def test_get_human_age_logic(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_get_human_age_negative_input() -> None:
    # Assuming negative age should return 0 or be handled gracefully as 0
    # based on 0,0 case.
    # If the logic is "if age < 15 return 0", negative fits.
    assert get_human_age(-1, -1) == [0, 0]


def test_get_human_age_type_error() -> None:
    # Checklist: "if the function receives an incorrect type...
    # it raises the correct exception."
    with pytest.raises(TypeError):
        get_human_age("15", 15)
    with pytest.raises(TypeError):
        get_human_age(15, "15")

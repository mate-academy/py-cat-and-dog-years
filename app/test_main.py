import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="returns zero if age is less than 15"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="returns 2 and more if age is more 23 "
        ),
        pytest.param(
            15, 23, [1, 1],
            id="returns 1 if age is between 15 and 23"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="returns 2 if age more 23"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="returns 3 and more"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="returns zero if age is negative"
        )
    ]
)
def test_modify_cats_and_dogs_ages(cat_age, dog_age, expected) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_raises_type_error_for_invalid_age() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
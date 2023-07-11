import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="negative cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14 cat/dog years should convert into 0 human age"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 cat/dog years should convert into 1 human age"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="if cat/dog years > 28/29 should return correctly values"
        )
    ]
)
def test_ages(
        cat_age: int,
        dog_age: int,
        expected_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "cat_age_str",
            "dog_age_str",
            TypeError,
            id="should raise error when cat/dog years is not integer"
        )
    ]
)
def test_raising_error_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

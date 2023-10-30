import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should add zeros with animal ages less than 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="add one when animal ages less than 24"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="add one more year when dog is 28, cat is 27"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="add one more year when dog is  28, cat is 27"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            -1, -1,
            ValueError,
            id="should raise value error when animal ages less than 0"
        ),
        pytest.param(
            "string", "string",
            ValueError,
            id="should raise value error when string is inputted"
        ),
        pytest.param(
            1.1, 1.1,
            ValueError,
            id="should raise value error when float is inputted"
        )
    ]
)
def test_get_human_age_invalid_input(
        cat_age: int,
        dog_age: int,
        expected_error: ValueError
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

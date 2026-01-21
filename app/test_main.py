import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="negative years cannot be converted in human age"
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero years cannot be converted in human age"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="first 14 cat/dog years give 0 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="cat/dog's age 15-23 should be equal to 1 human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="cat/dog's age 24-27 should be equal to 2 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="age conversion for an old cat and dog is incorrect"
        )
    ]
)
def test_age_calculation(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "cat_age_str",
            "dog_age_str",
            TypeError,
            id="should raise error when cat/dog years are not an integer"
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

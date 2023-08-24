import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "dog_age,cat_age,expected_result",
    [
        pytest.param(
            -1, 14,
            [0, 0],
            id="should return zero when age is less than 15"
        ),
        pytest.param(
            15, 23,
            [1, 1],
            id="should return 1 when age in range 15 and 23"
        ),
        pytest.param(
            28, 28,
            [3, 2],
            id="should tell apart cat and dog age conversion rates (4 and 5)"
        ),
        pytest.param(
            100, 100,
            [21, 17],
            id="should work with big numbers"
        )
        ]
)
def test_convert_age_correctly(
        dog_age,
        cat_age,
        expected_result
):
    assert get_human_age(dog_age, cat_age) == expected_result


@pytest.mark.parametrize(
    "dog_age,cat_age,expected_error",
    [
        pytest.param(
            "dog",
            "cat",
            TypeError,
            id="should raise TypeError if an argument is not numeric"
        )
    ]
)
def test_should_raise_type_error_when_wrong_argument(
        dog_age, cat_age, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(dog_age, cat_age)

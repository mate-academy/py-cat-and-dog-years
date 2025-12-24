import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_value",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return zero when age is zero"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return zero when age less than 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return 1 when value between 15 and 24"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return 1 when value between 15 and 24"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return 2 when value bigger than 24"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="should return 3 for 28/29 cat/dog years"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="should return 2 for 27/28 cat/dog years"
        ),
        pytest.param(
            -1, -2, [0, 0],
            id="should return 0 when values less than zero"
        ),
    ]
)
def test_convert_age_correctly(
        cat_age: int,
        dog_age: int,
        expected_value: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_value


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "0", 0, TypeError,
            id="should raise exception when cat age is not number"
        ),
        pytest.param(
            0, "0", TypeError,
            id="should raise exception when dog age is not number"
        ),
    ]
)
def test_raise_exception_correctly(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

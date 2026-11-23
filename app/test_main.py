from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, cat_human_age, dog_human_age",
    [
        pytest.param(
            0, 0, 0, 0,
            id="should be 0 if pet age < 15"
        ),
        pytest.param(
            14, 14, 0, 0,
            id="should be 0 if pet age < 15"
        ),
        pytest.param(
            15, 15, 1, 1,
            id="should be 1 if pet age in range(15, 24)"
        ),
        pytest.param(
            23, 23, 1, 1,
            id="should be 1 if pet age in range(15, 24)"
        ),
        pytest.param(
            24, 24, 2, 2,
            id="should be 1 if pet age in range(15, 24)"
        ),
        pytest.param(
            27, 28, 2, 2,
            id="should add 1 year for every next 4/5 years for cat/dog"
        ),
        pytest.param(
            28, 29, 3, 3,
            id="should add 1 year for every next 4/5 years for cat/dog"
        ),
        pytest.param(
            32, 34, 4, 4,
            id="should add 1 year for every next 4/5 years for cat/dog"
        ),
        pytest.param(
            100, 100, 21, 17,
            id="should add 1 year for every next 4/5 years for cat/dog"
        )
    ]
)
def test_human_age(
    cat_age: int,
    dog_age: int,
    cat_human_age: int,
    dog_human_age: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [cat_human_age, dog_human_age]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            "15", 20, TypeError,
            id="pet's age should be int"
        ),
        pytest.param(
            10, -5, ValueError,
            id="pet's age should be greater than 0"
        )
    ]
)
def test_raising_errors_correctly(
    cat_age: int,
    dog_age: int,
    expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

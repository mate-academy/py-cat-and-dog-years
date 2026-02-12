import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros if zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros less then 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return one more than 15"
        ),
        (
            24,
            24,
            [2, 2]
        ),
        (
            27,
            27,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            -1,
            -1,
            id="should raise exception if negative value"
        ),
        pytest.param(
            1000,
            10000,
            id="should raise exception if large number"
        )
    ]
)
def test_get_human_age_raising_value_error(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            "",
            "",
            id="should raise exception if non int value"
        )
    ]
)
def test_get_human_age_raising_type_error(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

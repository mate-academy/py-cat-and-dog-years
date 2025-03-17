from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="expected have 0, 0"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="expected have 1, 1"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="expected have 2, 2"),
        pytest.param(
            28,
            28,
            [3, 2],
            id="expected have 3, 2"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="expected have 21, 17")
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(
            "zero",
            8,
            id="str instead of cat_age"
        ),
        pytest.param(
            76,
            "nine",
            id="str instead of dog_age"
        ),
        pytest.param(
            None,
            5,
            id="None instead of cat_age"
        ),
        pytest.param(
            5,
            None,
            id="None instead of dog_age"
        )
    ]
)
def test_get_human_age_invalid_input(cat_age: int, dog_age: int,):
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age_incorrect,dog_age_incorrect,error",
    [
        ([], [], TypeError),
        (" ", " ", TypeError),
        ({}, {}, TypeError),
    ]
)
def test_raises_error_when_incorrect_data_type(
        cat_age_incorrect,
        dog_age_incorrect,
        error
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age_incorrect, dog_age_incorrect)

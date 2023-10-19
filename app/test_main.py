from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (27, 29, [2, 3]),
        pytest.param(
            0, 0, [0, 0], id="All animals ages are equal to zero"
        ),
        pytest.param(
            -30, -15, [0, 0], id="Ages are negative"
        ),
        pytest.param(
            90000, 12000, [22496, 2397], id="resive data out of normal range, too large numbers"
        )
    ]
)
def test_convert_cat_and_dog_age_with_correct_values(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(
            [21, 42, 62],
            "21",
            id="receives an incorrect type of data"
        )
    ]
)
def test_convert_cat_and_dog_age_with_incorrect_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

import pytest

from app.main import get_human_age


def test_arguments_should_be_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", {10})


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(-1, -2, [0, 0]),
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(27, 28, [2, 2]),
        pytest.param(28, 29, [3, 3]),
    ],
    ids=[
        "Zeros when ages are negative",
        "Zeros if ages are less than 15",
        "Ones if ages equal to 15",
        "Ones if ages less than 24",
        "Twos if ages are 27 and 28",
        "Threes if ages are 28 and 29"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    human_age_return = get_human_age(cat_age, dog_age)
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), (f"{cat_age} cat years should be {human_age_return[0]} human years and "
        f"{dog_age} dog years should be {human_age_return[1]} human years.\n"
        f"Got {human_age[0]} and {human_age[1]} instead")

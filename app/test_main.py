import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-5, 14, [0, 0], id="first 15 animals years"),
        pytest.param(15, 23, [1, 1], id="next 9 animals years"),
        pytest.param(24, 27, [2, 2], id="animals ages between 24 and 27"),
        pytest.param(100, 28, [21, 2], id="animals ages after 28")
    ]
)
def test_get_human_age_with_different_animals_age_ranges(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_should_raise_error_when_input_data_is_not_an_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", 10)

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(-60, -30, [0, 0], id="negative values of animals age"),
        pytest.param(0, 0, [0, 0], id="the age of the animals is 0"),
        pytest.param(14, 14, [0, 0], id="first 15 animals years"),
        pytest.param(23, 23, [1, 1], id="the next 9 animals years"),
        pytest.param(24, 24, [2, 2], id="animals age 24 years"),
        pytest.param(28, 28, [3, 2], id="animals age 28 years"),
        pytest.param(100, 100, [21, 17], id="animals age >28 years")
    ]
)
def test_get_human_age_with_animals_age(cat_age: int,
                                        dog_age: int,
                                        human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error_when_input_data_is_not_an_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", 12)

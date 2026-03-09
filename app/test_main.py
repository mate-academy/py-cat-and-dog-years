import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_ages"),
        pytest.param(14, 14, [0, 0], id="just_under_first_15_years"),
        pytest.param(15, 15, [1, 1], id="exactly_first_15_years"),
        pytest.param(23, 23, [1, 1], id="just_under_second_step_24"),
        pytest.param(24, 24, [2, 2], id="exactly_at_second_step_24"),
        pytest.param(27, 27, [2, 2], id="cat_and_dog_before_third_step_increments"),
        pytest.param(28, 28, [3, 2], id="cat_hits_third_step_first"),
        pytest.param(28, 29, [3, 3], id="dog_hits_third_step_at_29"),
        pytest.param(100, 100, [21, 17], id="large_integer_test"),
        pytest.param(-10, -10, [0, 0], id="negative_integers"),
    ]
)
def test_get_human_age_logic(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected

@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 15, id="string_cat_age"),
        pytest.param(15, 15.5, id="float_dog_age"),
        pytest.param(None, 24, id="none_type_input"),
    ]
)
def test_get_human_age_raises_error(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
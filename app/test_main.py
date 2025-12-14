import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0], id="both_zero"),
        pytest.param(14, 14, [0, 0], id="both_before_15"),
        pytest.param(15, 15, [1, 1], id="both_at_15"),
        pytest.param(23, 23, [1, 1], id="both_before_24"),
        pytest.param(24, 24, [2, 2], id="both_at_24"),
        pytest.param(27, 27, [2, 2], id="both_between_24_and_next_step"),
        pytest.param(28, 28, [3, 2], id="cat_steps_at_28"),
        pytest.param(100, 100, [21, 17], id="both_large_ages"),
    ],
)
def test_get_human_age_threshold_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(32, 34, [4, 4], id="independence_cat32_dog34"),
        pytest.param(40, 39, [6, 5], id="independence_cat40_dog39"),
    ],
)
def test_get_human_age_independence_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(-1, -1, [0, 0], id="both_negative"),
        pytest.param(-10, 0, [0, 0], id="cat_negative_dog_zero"),
        pytest.param(0, -5, [0, 0], id="cat_zero_dog_negative"),
        pytest.param(-100, 100, [0, 17], id="cat_negative_dog_large"),
        pytest.param(100, -100, [21, 0], id="cat_large_dog_negative"),
    ],
)
def test_get_human_age_negative_inputs(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("a", "b", id="both_strings"),
        pytest.param("10", 10, id="cat_string_dog_int"),
        pytest.param(10, "10", id="cat_int_dog_string"),
        pytest.param(10.5, 12.3, id="both_floats"),
        pytest.param(None, None, id="both_none"),
        pytest.param([], {}, id="list_and_dict"),
    ],
)
def test_get_human_age_raises_type_error_for_invalid_types(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)

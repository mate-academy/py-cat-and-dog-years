import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="zero_years"),
        pytest.param(14, 14, [0, 0], id="both_near_first_step_15"),
        pytest.param(15, 14, [1, 0], id="cat_15_dog_14"),
        pytest.param(14, 15, [0, 1], id="cat_14_dog_15"),
        pytest.param(15, 15, [1, 1], id="both_exactly_15_years"),
        pytest.param(16, 16, [1, 1], id="both_between_15_and_24"),
        pytest.param(23, 23, [1, 1], id="both_almost_24"),
        pytest.param(20, 17, [1, 1], id="mixed_ages_between_15_and_24"),
        pytest.param(24, 24, [2, 2], id="both_exactly_24_years"),
        pytest.param(24, 25, [2, 2], id="cat_24_dog_25"),
        pytest.param(25, 25, [2, 2], id="both_25"),
        pytest.param(26, 25, [2, 2], id="cat_26_dog_25"),
        pytest.param(27, 27, [2, 2], id="cat_27_dog_27"),
        pytest.param(28, 28, [3, 2], id="cat_28_dog_28"),
        pytest.param(28, 29, [3, 3], id="cat_28_dog_29"),
        pytest.param(100, 100, [21, 17], id="both_100_years"),
        pytest.param(500, 600, [121, 117], id="both_large_numbers"),
    ]
)
def test_should_convert_animals_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(-5, 10, id="negative_cat_age"),
        pytest.param(14, -9, id="negative_dog_age"),
        pytest.param(5, -5, id="both_ages_negative")
    ]
)
def test_should_raise_value_error_for_negative_ages(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_human_age(cat_age, dog_age)
    assert str(exc_info.value) == "cat_age and dog_age must be non-negative"


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("12", 10, id="cat_age_is_string"),
        pytest.param(12, "11", id="dog_age_is_string"),
        pytest.param(1.5, 5, id="cat_age_is_float"),
        pytest.param(16, 5.9, id="dog_age_is_float"),
        pytest.param(None, 17, id="cat_age_is_None"),
        pytest.param(10, None, id="dog_age_is_None"),
    ]
)
def test_should_raise_type_error_for_invalid_ages(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError) as exc_info:
        get_human_age(cat_age, dog_age)
    assert str(exc_info.value) == "cat_age and dog_age must be integers"

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="both_zero_animal_years_should_return_zero_human_years"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="below_first_threshold_returns_zero"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="exactly_first_threshold_returns_one_human_year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="just_before_two_human_years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="exactly_two_human_years"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="mid_second_range_still_two_years"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="cat_increases_faster_after_threshold"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="large_values_correct_human_years"
        ),
    ]
)
def test_human_age_conversion(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-1, 10, [0, 0], id="negative_cat_age_returns_zero"),
        pytest.param(10, -1, [0, 0], id="negative_dog_age_returns_zero"),
        pytest.param(-5, -5, [0, 0], id="both_negative_return_zeroes"),
    ]
)
def test_negative_values_allowed(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("15", 10, id="cat_age_string_raises_typeerror"),
        pytest.param(15, "10", id="dog_age_string_raises_typeerror"),
        pytest.param(None, 10, id="cat_age_none_raises_typeerror"),
        pytest.param(10, None, id="dog_age_none_raises_typeerror"),
    ]
)
def test_incorrect_types_raise_typeerror(
        cat_age: object,
        dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(3.14, 10, [0, 0], id="float_cat_age_behaves_as_number"),
        pytest.param(10, 2.71, [0, 0], id="float_dog_behaves_as_number"),
    ]
)
def test_float_values_do_not_raise(
        cat_age: float,
        dog_age: float,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected

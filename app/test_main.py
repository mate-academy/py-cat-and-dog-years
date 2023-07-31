import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_years",
    [
        pytest.param(
            -10,
            -20,
            [0, 0],
            id="negative_ages",
        ),
        pytest.param(
            0,
            0,
            [0, 0],
            id="zero_ages",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="14_cat_dog_years_to_0_human_years",
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15_cat_dog_years_to_1_human_year",
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23_cat_dog_years_to_1_human_year",
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24_cat_dog_years_to_2_human_years",
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="27_28_cat_dog_years_to_2_human_years",
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28_29_cat_dog_years_to_3_human_years",
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="big_ages_conversion",
        ),
    ]
)
def test_conversion_of_cat_and_dog_ages_to_human_years(
    cat_age: int, dog_age: int, expected_human_years: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_years


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param("12", "5", TypeError, id="invalid_data_type")
    ]
)
def test_invalid_data_type_check_for_ages(
    cat_age: int, dog_age: int, expected_exception: Exception
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)

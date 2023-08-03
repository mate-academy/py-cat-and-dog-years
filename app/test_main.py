import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="both_zero_age"),
    pytest.param(14, 14, [0, 0], id="both_under_15_years"),
    pytest.param(15, 15, [1, 1], id="both_15_years"),
    pytest.param(23, 23, [1, 1], id="both_just_over_15_years"),
    pytest.param(24, 24, [2, 2], id="both_exactly_1_more_year"),
    pytest.param(27, 27, [2, 2], id="both_just_over_1_more_year"),
    pytest.param(28, 28, [3, 2], id="cat_1_more_year_than_dog"),
    pytest.param(100, 100, [21, 17], id="both_just_over_2_more_years"),
    pytest.param(-1, -1, [0, 0], id="both_under_0_years")
])
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "10",
            10,
            TypeError,
            id="raise TypeError when years are not int"
        )
    ]
)
def test_raising_correct_errors(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)

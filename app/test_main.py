import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expect_result",
    [
        pytest.param(
            0, 0, [0, 0], id="test_input_ages_equal_0"
        ),
        pytest.param(
            1, 1, [0, 0], id="test_input_ages_equal_1"
        ),
        pytest.param(
            14, 14, [0, 0], id="test_input_ages_equal_14"
        ),
        pytest.param(
            15, 15, [1, 1], id="test_input_ages_equal_15"
        ),
        pytest.param(
            23, 23, [1, 1], id="test_input_ages_equal_23"
        ),
        pytest.param(
            24, 24, [2, 2], id="test_input_ages_equal_24"
        ),
        pytest.param(
            27, 27, [2, 2], id="test_input_ages_equal_27"
        ),
        pytest.param(
            28, 28, [3, 2], id="test_input_ages_equal_28"
        ),
        pytest.param(
            29, 29, [3, 3], id="test_input_ages_equal_29"
        )
    ]
)
def test_ages(cat_age: int, dog_age: int, expect_result: list) -> None:
    actual = get_human_age(cat_age, dog_age)
    assert actual == expect_result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(-1, -1, ValueError, id="should be raise ValueError"),
        pytest.param(200, 200, ValueError, id="should be raise ValueError"),
        pytest.param("15", 15, TypeError, id="should be raise TypeError"),
        pytest.param(14, "14", TypeError, id="should be raise TypeError")
    ]
)
def test_check_valid_input_data(cat_age: int,
                                dog_age: int,
                                expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        if (cat_age <= 0 or dog_age <= 0) or (cat_age > 150 or dog_age > 150):
            raise ValueError

        get_human_age(cat_age, dog_age)

import pytest
from app.main import get_human_age, convert_to_human


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_ages",
        [
            (0, 0, [0, 0]),
            (14, 15, [0, 1]),
            (24, 23, [2, 1]),
            (28, 27, [3, 2]),
            (32, 29, [4, 3]),
            (36, 34, [5, 4]),
            (100, 100, [21, 17]),
            pytest.param(-1, -1, [0, 0], id="age of cat/dog cannot be less than 0")
        ]
    )
    def test_get_human_age_expected_result(
            self,
            cat_age,
            dog_age,
            expected_human_ages
    ):
        assert get_human_age(cat_age, dog_age) == expected_human_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ([5], 2, TypeError),
            ("1", 1, TypeError),
            (2, {1}, TypeError),
            (3, "one", TypeError),
        ]
    )
    def test_raising_test_correctly(
            self,
            cat_age,
            dog_age,
            expected_error
    ):
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

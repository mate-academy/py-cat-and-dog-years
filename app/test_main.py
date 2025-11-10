from app.main import get_human_age

import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize(
        ("cat_age", "dog_age", "result"),
        [
            pytest.param(14, 14, [0, 0], id="2 normal ints"),
            pytest.param(0, 0, [0, 0], id="2 zeros"),
            pytest.param(15, 15, [1, 1], id="two 15 years"),
            pytest.param(23, 23, [1, 1], id="two 23 years"),
            pytest.param(27, 16, [2, 1],
                         id="less than boundary check for cat"),
            pytest.param(28, 16, [3, 1],
                         id="bigger than boundary check for cat"),
            pytest.param(16, 28, [1, 2],
                         id="less than boundary check for dog"),
            pytest.param(16, 29, [1, 3],
                         id="bigger than boundary check for dog"),
            pytest.param(24, 24, [2, 2], id="two 24 years"),
            pytest.param(-5, -6, [0, 0], id="2 negative numbers"),
            pytest.param(105, 120, [22, 21], id="2 really large numbers"),

        ],
    )
    def test_should_return_list_of_ages(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        ("cat_age", "dog_age", "expected_error"),
        [
            pytest.param((15,), 25, TypeError, id="tuple and int"),
            pytest.param("str", 25, TypeError, id="str and int"),
            pytest.param([25], 25, TypeError, id="list and int"),
        ],
    )
    def test_should_raise_error_if_parameter_has_wrong_data_type(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

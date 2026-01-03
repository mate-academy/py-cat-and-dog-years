import pytest

from app.main import get_human_age


class TestCatDog:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="get_human_age_receive_zero_list_when_args_zero"
            ),
            pytest.param
            (
                14, 5, [0, 0],
                id="receive_zero_list_when_args_less_than_15_years"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="receive_1_human_age_when_args_equal_15_years"
            ),
            pytest.param(
                15, 6, [1, 0],
                id="cat_receive_1_human_age_and"
                "_dog_0_when_args_equal_15_and_6_years"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="cat_and_dog_should_receive_1_when_age_is_23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="cat__and_dog_2_when_args_equal_24_years"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="cat_and_dog_should_receive_2_when_age_is_27"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="cat__receive_3_and_dog_2_when_args_equal_28_years"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="cat__receive_21_and_dog_17_when_args_equal_100_years"
            ),
            pytest.param(
                -2, -4, [0, 0],
                id="cat__receive_0_and_dog_0_when_args_less_then_0_years")
        ]
    )
    def test_modify_class_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_result: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "ert", "232", TypeError,
                id="should_raise_error_when_args_are_str"
            )
        ]
    )
    def test_raising_errors_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_error: type[Exception]
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

import pytest
from app.main import get_human_age


def test_should_return_list_of_int() -> None:
    result = get_human_age(15, 15)
    assert all(isinstance(val, int) for val in result)


class TestCheckNumberCases:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            # test_get_human_age_should_return_zeros_for_zero_ages
            (
                0, 0, [0, 0]
            ),
            # test_get_human_age_should_return_zeros_if_less_than_15
            (
                14, 14, [0, 0]
            ),
            # test_get_human_age_should_check_if_more_than_14_less_than_24
            (
                15, 15, [1, 1]
            ),
            # test_get_human_age_should_check_if_more_than_23_less_than_28
            (
                24, 24, [2, 2]
            ),
            # test_get_human_age_should_check_difference_between_cat_dog_ages
            (
                28, 28, [3, 2]
            ),
            # test_get_human_age_should_check_big_numbers
            (
                100, 100, [21, 17]
            )
        ]
    )
    def test_should_return_correct_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            ("a", 15, TypeError),
            (15, "a", TypeError),
            ("a", "a", TypeError),
            ({"a"}, {"a"}, TypeError),
            (["a"], ["a"], TypeError),
            (15.1, 15.2, TypeError),
            (-15, -16, ValueError)

        ]
    )
    def test_should_accept_correct_types(
            self, cat_age: int, dog_age: int, error: tuple
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)

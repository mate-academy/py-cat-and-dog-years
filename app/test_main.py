import pytest

from app.main import get_human_age


def test_get_human_age_should_return_list_with_two_element() -> None:
    goals = get_human_age(1, 1)
    assert isinstance(goals, list)


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return zero values for min args within its range"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zero values for max args within its range"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return both 1 value for min args within its range"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return both 1 value for max args within its range"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return both 2 value for min args within its range"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="should return both 2 value for max args within its range"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should return both 3 value for min args within its range"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return 21 and 17 for 100 in arguments"
            ),
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result


def test_get_human_age_should_return_zero_for_zero_in_input_for_both_cases()\
        -> None:
    goals = get_human_age(0, 0)
    assert goals == [0, 0]

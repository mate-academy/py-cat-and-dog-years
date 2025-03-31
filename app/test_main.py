import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_results",
        [
            pytest.param(
                0,
                0,
                [0, 0, ],
                id="Should return zero results",
            ),
            pytest.param(
                14,
                14,
                [0, 0, ],
                id=" maximum limit value for 0 human age"
            ),
            pytest.param(
                15,
                15,
                [1, 1, ],
                id="minimum limit value for 1 human age"
            ),
            pytest.param(
                23,
                23,
                [1, 1, ],
                id="maximum limit value for 1 human year"
            ),
            pytest.param(
                24,
                24,
                [2, 2, ],
                id="minimum limit value for 2 human years"
            ),
            pytest.param(
                27,
                27,
                [2, 2, ],
                id="maximum limit value for 2 human years"
            ),
            pytest.param(
                28,
                28,
                [3, 2, ],
                id="Checkin minimum limit value for 3 human years for cats"
            ),
            pytest.param(
                100000000,
                100000000,
                [24999996, 19999997],
                id="Checking big value"
            ),
            pytest.param(
                -20,
                -23123,
                [0, 0],
                id="Checking negative numbers"
            ),
        ]
    )
    def test_with_zero_values(self,
                              cat_age: int,
                              dog_age: int,
                              expected_results: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected_results


class TestGetHumanAgeDataType:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("0", 0),
            ("0", "0"),
            (None, 15),
            (None, None),
        ],
    )
    def test_with_wrong_types(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

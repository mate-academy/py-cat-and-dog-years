import pytest
from app.main import get_human_age


class TestHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="if animals age is 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="if animals age < 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="if animals age = 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="if animals age = 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="if animals age = 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="if animals age = 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="if animals age = 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="if animals age = 100"
            )
        ]
    )
    def test_convert_age_correctly(self, cat_age: int,
                                   dog_age: int,
                                   expected_human_age: list) -> None:

        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "15",
                "15",
                TypeError,
                id="should raise error if age is not int"
            ),
            pytest.param(
                -15,
                -15,
                ValueError,
                id="should raise error if age is < 0"
            ),
            pytest.param(
                101,
                101,
                ValueError,
                id="should raise error if age is > 100"
            )
        ]
    )
    def test_raising_errors_correctly(self,
                                      cat_age: int,
                                      dog_age: int,
                                      expected_error: Exception) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

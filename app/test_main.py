import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14, 14, [0, 0], id="should return 0 if pets age below 15"
            ),
            pytest.param(
                15, 15, [1, 1], id="should return 1 if pets age is 15"
            ),
            pytest.param(
                23, 23, [1, 1], id="should return 1 if pets age below 24"
            ),
            pytest.param(
                24, 24, [2, 2], id="should return 2 if pets age is 24"
            ),
            pytest.param(
                27, 28, [2, 2], id="should return 2 if cat age below 28 and dog age below 29"
            ),
            pytest.param(
                28, 29, [3, 3], id="should return 3 if cat age is 28 and dog age is 29"
            ),
            pytest.param(
                34, 45, [4, 6], id="should return correct age if cat age above 28 and dog age above 29"
            ),
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

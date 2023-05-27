import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14, 14, [0, 0], id="should return 0 if pets age unger first year threshold"
            ),
            pytest.param(
                15, 15, [1, 1], id="should return 1 if pets age at first year threshold"
            ),
            pytest.param(
                23, 23, [1, 1], id="should return 1 if pets age unger second year threshold"
            ),
            pytest.param(
                24, 24, [2, 2], id="should return 2 if pets age at second year threshold"
            ),
            pytest.param(
                27, 28, [2, 2], id="should return 2 if pets age unger third year threshold"
            ),
            pytest.param(
                28, 29, [3, 3], id="should return 3 if pets age at third year threshold"
            ),
            pytest.param(
                34, 45, [4, 6], id="should return correct age if pets age above third year threshold"
            ),
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age,
            dog_age,
            expected_result
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

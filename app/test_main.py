import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="both zero age"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="both under first threshold"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="both at first threshold"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="both under second threshold"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="both at second threshold"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="both under third threshold"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="cat enters third threshold"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="large age values"
            )
        ]
    )
    def test_get_human_age_different_threshold(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)

        assert result == expected_result

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_result",
        [
            pytest.param(
                13,
                13,
                [0, 0],
                id="should check age less 15"
            ),

            pytest.param(
                24,
                24,
                [2, 2],
                id="should check age, which consist of 15 + 9"
            ),

            pytest.param(
                28,
                28,
                [3, 2],
                id="should check years, which include extra years"
            ),

            pytest.param(
                100,
                100,
                [21, 17],
                id="should check few extra years"
            )

        ]
    )
    def test_converting_to_human_age_correctly(
            self,
            cat_years: int,
            dog_years: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_result

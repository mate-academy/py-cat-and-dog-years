import pytest


from app.main import get_human_age


class TestCheckDiffValues:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_years",
        [
            pytest.param(
                0, 0,
                [0, 0]
            ),
            pytest.param(
                14, 14,
                [0, 0]
            ),
            pytest.param(
                15, 15,
                [1, 1]
            ),
            pytest.param(
                23, 23,
                [1, 1]
            ),
            pytest.param(
                24, 24,
                [2, 2]
            ),
            pytest.param(
                27, 27,
                [2, 2]
            ),
            pytest.param(
                28, 28,
                [3, 2]
            ),
            pytest.param(
                100, 100,
                [21, 17]
            )
        ]
    )
    def test_should_return_correct_years(
            self,
            cat_years: int,
            dog_years: int,
            expected_years: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_years

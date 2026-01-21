import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_years,dog_years,expected_human_years",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="set both zeros"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="set both 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="set both 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="set both 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="set both 24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="set cat 27, dog 28"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="set cat 28, dog 29"
            ),
            # pytest.param(
            #     31,
            #     33,
            #     [3, 3],
            #     id="set cat 31, dog 33"
            # ),
            # pytest.param(
            #     32,
            #     34,
            #     [4, 4],
            #     id="set cat 32, dog 34"
            # )
        ]
    )
    def test_set_age_correctly(
            self,
            cat_years: int,
            dog_years: int,
            expected_human_years: list[int, int]) -> None:
        assert get_human_age(cat_years, dog_years) == expected_human_years

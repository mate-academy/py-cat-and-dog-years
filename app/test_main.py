import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero ages - both animals start at zero"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="just before first age milestone - no aging progression"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="at first aging milestone - cats and dogs age by 1 year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="at second aging milestone - cats and dogs age by 2 years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="beyond second milestone - cat ages faster than dog"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="advanced ages - cats and dogs in later life stages"
            ),
            pytest.param(
                -10,
                -10,
                [0, 0],
                id="negative ages input - invalid ages set to zero"
            ),

        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

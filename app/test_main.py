import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return 0 human age when cat/dog 0...15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 human age when cat/dog 15...24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 human age when cat/dog 24...28/29"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return 21/17 when animal have extra human years"
            )
        ]
    )
    def test_count_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> bool:
        assert get_human_age(cat_age, dog_age) == expected_result

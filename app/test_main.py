import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, convert_to_human",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test: if animal age in human years is 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test: if animal age in human years is closely to 1"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test: if animal age in human years is 1"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test: if animal age in human years is 2"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="test: if animal age in human years is 3"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test: if animal age is 100"
            )
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age,
            dog_age,
            convert_to_human
    ):
        assert get_human_age(cat_age, dog_age) == convert_to_human

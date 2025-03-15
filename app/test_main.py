import pytest

from app.main import get_human_age


class TestHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="years equal to zero"
            ),
            pytest.param(
                23,
                20,
                [1, 1],
                id="test age above fifteen"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="test age above 24"
            ),
            pytest.param(
                28,
                24,
                [3, 2],
                id="extra years for cats"
            ),
            pytest.param(
                24,
                29,
                [2, 3],
                id="extra years for dogs"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="large numbers"
            )
        ]
    )
    def test_get_human_age(self, cat_age: int, dog_age: int, result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

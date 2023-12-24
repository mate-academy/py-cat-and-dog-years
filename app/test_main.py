import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list with zero ages."
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="list with zero ages, cat_age and dog_age < 15."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="list with ages, cat_age and dog_age == 15"

            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="list with ages, cat_age and dog_age > 15"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="list with ages, cat_age and dog_age == 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="list with ages, cat_age and dog_age > 24"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="list with ages, cat_age == 28  dog_age > 24"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="list with ages, cat_age > 28  dog_age > 29]"
            )
        ]
    )
    def test_get_human_age(self, cat_age: int,
                           dog_age: int,
                           expected_age: list):

        assert get_human_age(cat_age, dog_age) == expected_age

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_ages",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return 0 human years if animal age is 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return 0 human years if animal age is 1-14"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return 1 human year if animal age is 15-23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return 2 human years if cat age is 24-27"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return 2 human years if dog age is 24-28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should add 1 human year per each 4 cat years "
                   "if cat age is 24+"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should add 1 human year per each 5 dog years "
                   "if dog age is 24+"
            ),
            pytest.param(
                -1, -1, [0, 0],
                id="should return 0 if animal age is a negative integer"
            )
        ]
    )
    def test_give_correct_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_ages

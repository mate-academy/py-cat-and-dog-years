import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_ages, dog_ages, human_age",
        [
            pytest.param(
                0, 0,
                [0, 0],
                id="When age human and animals equal"
            ),
            pytest.param(
                14, 14,
                [0, 0],
                id="Still animals age equal 0 human ages"
            ),
            pytest.param(
                15, 15,
                [1, 1],
                id="When animals ages equal 1 human ages"
            ),
            pytest.param(
                23, 23,
                [1, 1],
                id="When animals ages equal 1 human ages"
            ),
            pytest.param(
                24, 24,
                [2, 2],
                id="When animals ages equal 2 human ages"
            ),
            pytest.param(
                28, 29,
                [3, 3],
                id="When animals ages equal 3 human ages"
            ),
        ]
    )
    def test_cats_and_dogs_ages_in_human_convert(
            self,
            cat_ages: int,
            dog_ages: int,
            human_age: list) -> None:
        assert get_human_age(cat_ages, dog_ages) == human_age

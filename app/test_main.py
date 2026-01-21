from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="should correct age for negative number or 0"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should correct age for the first 15 years"
            ),
            pytest.param(
                24,
                25,
                [2, 2],
                id="should return correct age for next 9 years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return correct age for every 4 years after"
            ),
            pytest.param(
                29,
                29,
                [3, 3],
                id="should return correct age for every 5 years after"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test should work with large number"
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    def test_get_correct_date_type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("cat_age", 3.6)

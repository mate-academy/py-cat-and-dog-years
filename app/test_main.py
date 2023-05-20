import pytest

from app.main import get_human_age


class TestConvertAnimalAgeToHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="human age is zero when cat and dog ages are both zero"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="human age is one when cat and dog ages are both 23"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="human age is zero when cat and dog ages are both 14"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="human age is 2 when cat and dog ages are both 24"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="human age is 21 and 17 when cat and dog ages are both 100"
            )
        ]
    )
    def test_convert_animal_age_to_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        human_age_result = get_human_age(cat_age, dog_age)
        assert human_age_result == human_age

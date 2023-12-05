import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should be 0 when 'animal_age' < 15"
            ),
            pytest.param(
                15,
                23,
                [1, 1],
                id="should be 1 when 15 <= 'animal_age' < 24"
            ),
            pytest.param(
                24,
                27,
                [2, 2],
                id="should be 2 when 24 <= 'animal_age' <= 29"
            ),
            pytest.param(
                48,
                48,
                [8, 6],
                id="should be correct value"
            )
        ]
    )
    def test_convert_animal_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: int

    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

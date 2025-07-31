import pytest

from app.main import get_human_age
from app.main import convert_to_human


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0,0,[0, 0],
                id="should return list of zeros when both ages are zero"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should work fine for both ages equal to first year"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should work fine for both ages greater than 15"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should work fine for both ages greater than 24"
            ),
            pytest.param(
                28, 29, [3, 4],
                id="should work fine for both ages greater than 24 with different values"
            )

        ],
    )
    def test_get_human_age(self, cat_age, dog_age, human_age):
        assert get_human_age(cat_age, dog_age) == human_age


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "animal_age, first_year, second_year, each_year, expected",
        [
            pytest.param(0, 15, 9, 4, 0, id="age less than first year"),
            pytest.param(15, 15, 9, 4, 1, id="age equal to first year"),
            pytest.param(24, 15, 9, 4, 2, id="age equal to first + second year"),
            pytest.param(28, 15, 9, 4, 3, id="age after first + second year"),
        ],
    )
    def test_convert_to_human(
            self,
            animal_age,
            first_year,
            second_year,
            each_year,
            expected
    ):

        assert convert_to_human(
            animal_age,
            first_year,
            second_year,
            each_year
        ) == expected

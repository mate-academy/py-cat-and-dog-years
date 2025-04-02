from app.main import get_human_age
import pytest


class TestConvertAnimalToHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test animal age 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test animal age 14"
            ),
            pytest.param(
                20,
                21,
                [1, 1],
                id="test animal age above 15"
            ),
            pytest.param(
                25,
                26,
                [2, 2],
                id="test animal age above 24"
            ),
            pytest.param(
                20,
                30,
                [1, 3],
                id="test extra years for dog"
            ),
            pytest.param(
                33,
                23,
                [4, 1],
                id="test extra years for cat"
            ),
            pytest.param(
                70,
                45,
                [13, 6],
                id="just a test"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test elder age"
            ),
            pytest.param(
                133,
                122,
                [29, 21],
                id="test vast age"
            ),
            pytest.param(
                -7,
                -2,
                [0, 0],
                id="test negative age"
            ),

        ]
    )
    def test_convert_to_human_age(self,
                                  cat_age: int,
                                  dog_age: int,
                                  expected_human_age: list)\
            -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

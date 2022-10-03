import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, ages_of_cat_and_dog_to_human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test should return zeros when ages equal 0"
            ),
            pytest.param(
                14,
                2,
                [0, 0],
                id= "Test should return zeros when ages less than 15"
            ),
            pytest.param(
                23,
                24,
                [1, 2],
                id="Test should return correct output for different ages"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Test should return different result for 28 pets ages"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Test for larger ages"
            ),
            pytest.param(
                -213,
                -523423,
                [0, 0],
                id="Test should return zeros for ages less than 0"
            )
        ]
    )
    def test_get_human_age_from_ages_of_cat_and_dog(
            self,
            cat_age,
            dog_age,
            ages_of_cat_and_dog_to_human_age
    ):
        assert (
                get_human_age(cat_age, dog_age)
                ==
                ages_of_cat_and_dog_to_human_age
        )

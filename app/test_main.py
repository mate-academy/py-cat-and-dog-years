import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "init_cat_age,init_dog_age,expected_list_of_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeros list if the initial values are 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zeros list if the initial values are < 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return 1 year list if the initial "
                   "values are more than 15 and less than 24"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 year list if the initial "
                   "values are  less than 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 year list if the initial values are 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return 2 year list if the initial values are 27, 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return 3 for cat and 2 years for dog if "
                   "the initial values are 28, 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return 21 years for cat and 17 years for dog if "
                   "the initial values are 100, 100"
            ),
        ]
    )
    def test_get_human_age(
            self,
            init_cat_age: int,
            init_dog_age: int,
            expected_list_of_age: list
    ) -> None:
        assert (get_human_age(init_cat_age, init_dog_age)
                == expected_list_of_age)

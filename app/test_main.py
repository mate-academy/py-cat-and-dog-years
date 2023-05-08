import pytest
from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list with list [0, 0]"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return list with list [0, 0]"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return list with list [1, 1]"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return list with list [1, 1]"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return list with list [2, 2]"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return list with list [21, 17]"
            )
        ]
    )
    def test_get_human_age_result(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                -1,
                2,
                ValueError,
                id="Cat_age and Dog_age should be equal to positive values"
            ),
            pytest.param(
                2,
                -7,
                ValueError,
                id="Cat_age and Dog_age should be equal to positive values"
            ),
            pytest.param(
                "23",
                "hello",
                TypeError,
                id="Cat_age and Dog_age should have type int not str"
            )
        ]
    )
    def test_raising_errors(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: ValueError | TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

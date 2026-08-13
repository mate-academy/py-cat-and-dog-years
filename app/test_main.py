import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result,expected_exception",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                None,
                id="should return [0, 0] for 0, 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                None,
                id="should return [1, 1] for 14, 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                None,
                id="should return [1, 1] for 15, 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                None,
                id="should return [1, 1] for 23, 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                None,
                id="should return [2, 2] for 24, 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                None,
                id="should return [2, 2] for 27, 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                None,
                id="should return [3, 2] for 28, 28"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                None,
                id="should return [21, 17] for 100, 100"
            ),
            pytest.param(
                "Error",
                "Error",
                None,
                TypeError,
                id="should return Type Exception"
            ),
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int | str,
            dog_age: int | str,
            expected_result: int,
            expected_exception: Exception
    ) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                get_human_age(cat_age, dog_age)
        else:
            assert get_human_age(cat_age, dog_age) == expected_result

import pytest
from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                14, 14, [0, 0],
                id="correct age limit value before 15, list with 2 elements"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="correct age limit value after 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="correct age limit value before 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="correct age limit value after 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="correct age limit value for cat before 28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="correct age limit value for cat "
                   "after 28 and for dog before 29"
            ),
            pytest.param(
                30, 29, [3, 3],
                id="correct age limit value for dog after 29"
            ),
            pytest.param(
                -1, -6, [0, 0],
                id="values less than 0"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="0 age"
            ),
            pytest.param(
                9999999, 123456789, [2499995, 24691355],
                id="large numbers"
            ),
            pytest.param(
                11.1, 12.1, [0, 0],
                id="should return 0 if parameters is float"
            )
        ]
    )
    def test_correct_age_output(
            self,
            cat_age: int,
            dog_age: int,
            result: list[int]
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == result
        ), f"{cat_age} cat age and {dog_age} dog age " \
           f"should be equal to {result} human age"

    @pytest.mark.parametrize(
        "cat_age,dog_age,exception",
        [
            pytest.param(
                "12", "eleven", TypeError,
                id="rise error if `cat_age` or `dog_age` is incorrect type"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: Any,
            dog_age: Any,
            exception: Exception
    ) -> None:
        with pytest.raises(exception):
            get_human_age(cat_age, dog_age)

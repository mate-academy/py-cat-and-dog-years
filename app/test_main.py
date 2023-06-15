import pytest
from app.main import get_human_age


class TestAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                -1, -1, [0, 0],
                id="Return 0 when age is negative"
            ),

            pytest.param(
                0, 0, [0, 0],
                id="Return 0"
            ),

            pytest.param(
                14, 14, [0, 0],
                id="Return 0 when cat or dog age less than 15"
            ),

            pytest.param(
                15, 15, [1, 1],
                id="Return 1 when cat or dog age 15"
            ),

            pytest.param(
                23, 23, [1, 1],
                id="Return 1 when cat or dog age less than 24"
            ),

            pytest.param(
                24, 24, [2, 2],
                id="Return 2 when cat or dog age 24"
            ),

            pytest.param(
                27, 27, [2, 2],
                id="Return 2 when cat or dog age 27"
            ),

            pytest.param(
                28, 28, [3, 2],
                id="Return 3 for cat and 2 for dog"
            ),

            pytest.param(
                100, 100, [21, 17],
                id="Every 4 next cat and 5 next dog years equal "
                   "to 1 extra human year"
            ),
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param("one", 1, TypeError, id="Error when input incorrect"),
            pytest.param([30], [6], TypeError, id="Error when input incorrect")
        ]
    )
    def test_raising_errors(self,
                            cat_age: int,
                            dog_age: int,
                            result: type[Exception]) -> None:
        with pytest.raises(result):
            get_human_age(cat_age, dog_age)

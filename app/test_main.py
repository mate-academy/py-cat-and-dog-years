import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Human age is zero when pets age are zero",
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Human age is zero when pets age < 15"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Human age is 2 when pets age == 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Human age is 2 when pets age == 27"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Human age is 3 when cat age is 28 and dog age 29",
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="100 in Human age when cat is 21 and dog is 17",
            ),
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="Human age is zero when pets age is negative"
            )
        ],
    )
    def test_output_value(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age", [(1, " "), (" ", 1), (" ", " ")]
    )
    def test_wrong_input_value(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

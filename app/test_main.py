import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_output",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (100, 100, [21, 17]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3])
        ],
        ids=[
            "check output if receive negative numbers",
            "check output if receive zero numbers",
            "check output if receive large numbers",
            "check edged situation: cat age 14, dog age 14",
            "check edged situation: cat age 15, dog age 15",
            "check edged situation: cat age 23, dog age 23",
            "check edged situation: cat age 24, dog age 24",
            "check edged situation: cat age 27, dog age 28",
            "check edged situation: cat age 28, dog age 29",
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_output: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_output

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("27", 28, TypeError),
            (27, [28], TypeError),
            ("27", "28", TypeError)
        ],
        ids=[
            "raise exception when receive incorrect type of data",
            "raise exception when receive incorrect type of data",
            "raise exception when receive incorrect type of data",
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (23, 23, [1, 1]),
            (28, 29, [3, 3]),
            (27, 28, [2, 2]),
            (-28, -29, [0, 0]),
            (100, 100, [21, 17]),
            (1000, 1000, [246, 197]),
            (00, 00, [0, 0]),

        ],
        ids=["when providing cat dog age 0",
             "when providing cat dog age 14",
             "when providing cat dog age 23",
             "when providing cat dog age 28 29",
             "when providing cat dog age 27 28",
             "when providing cat dog age data out of range",
             "when providing cat dog age 100, 100",
             "when providing cat dog age 1000, 1000",
             "when providing cat dog age 00 00"
             ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("15", 10),
            (10, "25"),
            (None, 35),
            (0, None),
            ("fifty", "hundred"),
            ([100], [150]),
        ],
        ids=[
            "when providing cat age as a string",
            "when providing dog age as a string",
            "when providing cat age as a Type",
            "when providing dog age as a Type",
            "when providing cat age and dog age as a strings",
            "when providing cat age and dog age as lists",
        ]
    )
    def test_get_human_age_incorrect_type_provided(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

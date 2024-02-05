from typing import Any, Type

import pytest

from app.main import get_human_age


class TestLogicalErrors:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (5, 15, [0, 1]),
            (88, 57, [18, 8]),
            (66, 33, [12, 3]),
        ],
        ids=[
            "Should return [0, 0], if cat age and dog age are negative",
            "Should return [0, 0], if cat age and dog age are lower then 15",
            "Should return [1, 1], if cat age and dog age equal 15",
            "Should return [1, 1], if cat age and dog age "
            "are more then 14 and lower then 24",
            "Should return [1, 1], if cat age and dog age "
            "are more then 14 and lower then 24",
            "Should return [2, 2], if cat age and dog age "
            "are more then 14 and lower then 28",
            "Should return [2, 2], if cat age and dog age "
            "are more then 14 and lower then 28",
            "Should return [3, 2], if cat age - 28 and dog age - 28",
            "Should return [21, 17], if cat age - 21 and dog age - 17",
            "Should return [0, 1], if cat age - 5 and dog age - 15",
            "Should return [18, 8], if cat age - 88 and dog age - 57",
            "Should return [12, 3], if cat age - 66 and dog age - 33"
        ]
    )
    def test_correspondence_of_human_years_to_animals(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == human_age
        ), (f"\'Cat age\' - {cat_age} and \'dog age\' - {dog_age} "
            f"should be equal to {human_age}")


class TestDataTypes:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            ("1", "1", TypeError),
            ([], [], TypeError),
            ({}, {}, TypeError),
            (None, None, TypeError),
        ],
        ids=[
            "input type should be integer",
            "input type should be integer",
            "input type should be integer",
            "input type should be integer"
        ]
    )
    def test_checking_for_entered_data_types(
            self,
            cat_age: Any,
            dog_age: Any,
            expected: Type[Exception]
    ) -> None:
        with pytest.raises(expected):
            get_human_age(cat_age, dog_age)

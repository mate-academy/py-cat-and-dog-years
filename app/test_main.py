import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_age",
        [
            (1, 1, [0, 0]),
            (14, 14, [0, 0]),
            (14, 15, [0, 1]),
            (15, 14, [1, 0]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "cat 1 year and dog 1 year equal to human age 0",
            "cat 14 years and dog 14 years equal to human age 0",
            "cat 14 years and dog 15 years equal to human age 0 and 1",
            "cat 15 years and dog 14 years equal to human age 1 and 0",
            "cat 23 years and dog 23 years equal to human age 1",
            "cat 24 years and dog 24 years equal to human age 2",
            "cat 27 years and dog 27 years equal to human age 2",
            "cat 28 years and dog 28 years equal to human age 3 and 2",
            "cat 29 years and dog 29 years equal to human age 3",
            "cat 100 years and dog 100 years equal to human age 21 and 17",
        ],
    )
    def test_cat_and_dog_age_equal_to_human_age(
        self, cat_age: int, dog_age: int, expected_human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

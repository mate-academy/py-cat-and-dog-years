import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            (1, 1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "from 0 to 14 cat and dog years give 0 human year",
            "from 0 to 14 cat and dog years give 0 human year",
            "first 15 cat and dog years give 1 human year",
            "from 15 to 23 cat and dog years give 1 more human year",
            "after 23 years every 4 next cat years give 1 extra human year",
            "after 23 years every 5 next dog years give 1 extra human year",
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("1", 1, TypeError),
            (2, "2", TypeError),
        ],
        ids=[
            "cat age must be an integer",
            "dog age must be an integer",
        ]
    )
    def test_get_human_age_error(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: TypeError
    ) -> None:

        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

import pytest

from app.main import get_human_age


class TestCatDogYears:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test should return zero ages when cat and dog age == 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test should return zero ages when cat and dog age < 15"),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test should return 1 ages when cat and dog age >= 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test should return 1 ages when cat and dog age <= 23"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test should return 2 ages when cat and dog age == 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="test should return 2 ages when cat and dog age == 27"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id=""
                   "test should return "
                   "3 cat age and 2 dog age "
                   "when cat and dog age == 28"
            )
        ]
    )
    def test_all_cases(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

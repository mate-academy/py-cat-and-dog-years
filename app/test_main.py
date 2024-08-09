import pytest

from app.main import get_human_age


class TestGetAge:
    @pytest.mark.parametrize(
        "dog_age, cat_age, excepted_age, description",
        [
            (0, 0, [0, 0], "Both ages are zero"),
            (
                14, 14, [0, 0],
                "Both ages below the threshold for human years conversion"
            ),
            (15, 15, [1, 1], "Minimum age for first human age"),
            (
                23, 23, [1, 1],
                "Age just below the next human year conversion."
            ),
            (24, 24, [2, 2], "Second human year"),
            (
                27, 27, [2, 2],
                "Age just below the third human year for dogs"
            ),
            (28, 28, [3, 2], "Third year for dog, but not cat"),
            (100, 100, [21, 17], "High age for both dog and cat"),
        ]
    )
    def test_correctly_age(
            self,
            dog_age: int,
            cat_age: int,
            excepted_age: list,
            description: str
    ) -> None:
        assert get_human_age(dog_age, cat_age) == excepted_age

    @pytest.mark.parametrize(
        "dog_age, cat_age, exception_type, description",
        [
            (-3, 15, ValueError, "If dog age negative - raise ValueError"),
            (10, -1, ValueError, "If cat age negative - raise ValueError"),
            ("ten", 10, TypeError, "Non-integer raise TypeError"),
            (10, "eight", TypeError, "Non-integer raise TypeError."),
        ]
    )
    def test_invalid_inputs(
            self,
            dog_age: int,
            cat_age: int,
            exception_type: type,
            description: str
    ) -> None:
        with pytest.raises(exception_type, match=description):
            get_human_age(dog_age, cat_age)

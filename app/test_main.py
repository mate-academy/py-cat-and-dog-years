import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_age",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (15, 15, [1, 1]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (10000000, 10000000, [2499996, 1999997]),
        ],
        ids=[
            "-1 cat and dog years should give 0 human years",
            "0 cat years and 0 dog years should give 0 human years",
            "15 cat years and 15 dog years should give 1 human year",
            "27 cat years and 27 dog years should "
            "give 2 human year",
            "28 cat years should give 3 and dog"
            " 28 years should give 2 human years",
            "28/29 cat/dog years should convert into 3 human age.",
            "100 cat years and 100 dog years"
            " should give 2 human years",
            "10000000 cat years should return 2499996 and "
            "10000000 dog years should give 1999997 human years",
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_human_age: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            ("20", 20, TypeError),
            (20, "20", TypeError),
        ],
        ids=[
            "cat age must be int",
            "dog age must be int",
        ],
    )
    def test_errors_for_not_int_values(self,
                                       cat_age: int,
                                       dog_age: int,
                                       error: TypeError) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

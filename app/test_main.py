import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            (-1, -2, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (16, 16, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "Invalid input should return 0",
            "(0,0) cat/dog years should be convert to [0,0]",
            "(14,14) cat/dog years should be convert to [0,0]",
            "(15,15) cat/dog years should be convert to [1,1]",
            "(16,16) cat/dog years should be convert to [1,1]",
            "(23,23) cat/dog years should be convert to [1,1]",
            "(24,24) cat/dog years should be convert to [2,2]",
            "(27,27) cat/dog years should be convert to [2,2]",
            "(28,28) cat/dog years should be convert to [3,2]",
            "(100,100) cat/dog years should be convert to [21,17]",
        ],
    )
    def test_convert_to_human_age_correct(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            ("12", 14),
            (12, "14"),
        ],
        ids=[
            "should raise error if cat_age/dog_age is number",
            "should raise error if cat_age/dog_age is number"
        ]
    )
    def test_rising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

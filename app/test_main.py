import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,cat_human_years,dog_human_years",
        [
            (0, 0, 0, 0),
            (15, 15, 1, 1),
            (23, 23, 1, 1),
            (24, 24, 2, 2),
            (28, 29, 3, 3),
            (100, 100, 21, 17),
        ],
        ids=[
            "less than first limit should convert to 0",
            "first limit should convert to 1",
            "less than second limit should convert to 1",
            "second limit should convert to 2",
            "third limit should convert to 3",
            "much bigger than second limit should convert to different"
        ]
    )
    def test_convert_ages_correctly(
            self,
            cat_age: int,
            dog_age: int,
            cat_human_years: int,
            dog_human_years: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [
            cat_human_years,
            dog_human_years
        ]

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
            (-1, -1, 0, 0),
        ],
        ids=[
            "less than first limit should convert to 0",
            "first limit should convert to 1",
            "less than second limit should convert to 1",
            "second limit should convert to 2",
            "third limit should convert to 3",
            "much bigger than second limit should convert to different",
            "negative values should convert to 0s",
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

    @pytest.mark.parametrize(
        "cat_ages,dog_ages,expected_error",
        [
            ("", 1, TypeError),
            (1, "", TypeError),
        ],
        ids=(
            "should raise type error if 'cat_age' is not a number",
            "should raise type error if 'dog_age' is not a number",
        )
    )
    def test_raising_errors_correctly(
            self,
            cat_ages: str | int,
            dog_ages: str | int,
            expected_error: type[BaseException]
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_ages, dog_ages)

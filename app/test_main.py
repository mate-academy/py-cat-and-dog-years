from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expected_years_list",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-2, 0, [0, 0]),
            (1000, 1245, [246, 246])
        ],
        ids=[
            "0 cat/dog years should convert into 0 human age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/27 cat/dog years should convert into 2 human age.",
            "28/28 cat/dog years should convert into 3/2 human age.",
            "100/100 cat/dog years should convert into 21/17 human age.",
            "-2/0 cat/dog years should convert into 0 human age.",
            "1000/1245 cat/dog years should convert into 246 human age."
        ]
    )
    def test_get_correctly_human_age(
        self,
        cat_years: int,
        dog_years: int,
        expected_years_list: list[int]
    ) -> None:
        assert get_human_age(cat_years, dog_years) == expected_years_list

    @pytest.mark.parametrize(
        "cat_years, dog_years, expected_error",
        [
            ("1", 2, TypeError),
            (None, 0, TypeError),
        ],
        ids=[
            "should return TypeError",
            "should return TypeError",
        ]
    )
    def test_get_correct_error(
        self,
        cat_years: any,
        dog_years: any,
        expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_years, dog_years)

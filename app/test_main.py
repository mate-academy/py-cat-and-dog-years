import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (-1, -1, [0, 0],),
            (0, 0, [0, 0],),
            (14, 14, [0, 0],),
            (15, 15, [1, 1],),
            (23, 23, [1, 1],),
            (24, 24, [2, 2],),
            (27, 28, [2, 2],),
            (28, 29, [3, 3],),
            (100, 100, [21, 17],),
        ],
        ids=[
            "Negative age.",
            "Zero age.",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/28 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "Maximum variables."
        ]
    )
    def test_normal_variables_age(self, cat_age: int,
                                  dog_age: int,
                                  result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_type_error_age(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("cat_age", "dog_age")

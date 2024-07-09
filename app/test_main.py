import pytest

from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "age_cat, age_dog, result",
        [
            (-100, -100, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17])
        ], ids=[
            "negative conditions",
            "zero conditions",
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/28 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age.",
            "maximum conditions"
        ]
    )
    def test_normal_age(self, age_cat: int, age_dog: int,
                        result: list[int, int]) -> None:
        assert get_human_age(age_cat, age_dog) == result

    def test_out_of_normal_age(self) -> None:
        with pytest.raises(TypeError):
            assert get_human_age("a", "b")

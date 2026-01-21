import pytest
from app.main import get_human_age


class TestConvertHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [3, 2]),
            (29, 28, [3, 3]),
        ],
        ids=[
            "14 cat/dog years should convert into 0 human age.",
            "15 cat/dog years should convert into 1 human age.",
            "23 cat/dog years should convert into 1 human age.",
            "24 cat/dog years should convert into 2 human age.",
            "27/28 cat/dog years should convert into 2 human age.",
            "28/29 cat/dog years should convert into 3 human age."
        ]
    )
    def test_convert_human_age(self,
                               dog_age: int,
                               cat_age: int,
                               expected: list
                               ) -> None:

        assert get_human_age(dog_age, cat_age) == expected


class TestInvalidInputType:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("string", 10),
            (10, "string"),
            ("string", "string")
        ]
    )
    def test_invalid_input_type(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

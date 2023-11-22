import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,converted_cat_age,converted_dog_age",
        [
            (0, 0, 0, 0),
            (14, 14, 0, 0),
            (15, 15, 1, 1),
            (24, 24, 2, 2),
            (28, 29, 3, 3),
            (100, 100, 21, 17)
        ],
        ids=["0 cat/dog years should convert into 0 human age.",
             "14 cat/dog years should convert into 0 human age.",
             "15 cat/dog years should convert into 1 human age.",
             "24 cat/dog years should convert into 2 human age.",
             "28/29 cat/dog years should convert into 3/3 human age.",
             "100/100 cat/dog years should convert into 21/17 human age."
             ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            converted_cat_age: int,
            converted_dog_age: int
    ) -> None:
        assert (
                get_human_age(cat_age, dog_age)
                == [converted_cat_age, converted_dog_age]
        )

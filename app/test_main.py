import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (15, 15, [1, 1]),
            (14, 14, [0, 0]),
            (-1, -1, [0, 0]),
            (-24, -24, [0, 0]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (32, 32, [4, 3]),
            (70, 70, [13, 11]),
            (100, 100, [21, 17]),
            (200, 200, [46, 37]),
        ]
    )
    def test_human_age_by_cat_dog(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_incorrect_type_for_dog(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(1, "1")

    def test_incorrect_type_for_cat(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)

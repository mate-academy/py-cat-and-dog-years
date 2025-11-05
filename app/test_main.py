import pytest
from app.main import get_human_age


class TestCatAndDogs:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (
                0, 0, [0, 0],
            ),
            (
                14, 14, [0, 0],
            ),
            (
                15, 15, [1, 1],
            ),
            (
                23, 23, [1, 1],
            ),
            (
                24, 24, [2, 2],
            ),
            (
                27, 27, [2, 2],
            ),
            (
                28, 28, [3, 2],
            ),
            (
                100, 100, [21, 17],
            ),
            (
                -10, -5, [0, 0],
            ),
        ]
    )
    def test_check_cat_and_dogs_year(
            self,
            cat_age: int,
            dog_age: int,
            human_age: int,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    def test_convert_age_invalid_type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("asdasd", -5)

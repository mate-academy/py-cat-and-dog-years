import pytest
from app.main import get_human_age


class TestAgeConvert:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                -5, -10, [0, 0],
                id="should return zeros when age is negative"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="should return zeros when age is zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return zeros when cat and dog age less than 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="cat and dog age convert when age less than 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="cat and dog age convert when age greater than 23"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="cat and dog age convert when age greater than 27"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="cat and dog age convert when age is a big number"
            )
        ]
    )
    def test_cat_and_dog_age_convert_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


def test_should_raise_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("15", "25")

import pytest

from typing import Union

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,convert_to_human_age",
        [
            pytest.param(
                14, 14, [0, 0], id="1 <= ages < 15"
            ),
            pytest.param(
                23, 23, [1, 1], id="15 <= ages animal < 24"
            ),
            pytest.param(
                25, 25, [2, 2], id="24 <= ages animal < 28"
            ),
            pytest.param(
                28, 29, [3, 3], id="28 <= cat age, 24 <= dog age < 29"
            ),
            pytest.param(
                120, 94, [26, 16], id="max animals ages"
            ),
            pytest.param(
                -1, 1, [0, 0], id="when cat age lower than 0"
            ),
            pytest.param(
                1, -1, [0, 0], id="when dog age lower than 0"
            ),
            pytest.param(
                0, 0, [0, 0], id="when ages equal 0"
            )
        ]
    )
    def test_calculate_ages(
            self,
            cat_age: int,
            dog_age: int,
            convert_to_human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == convert_to_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "18",
                5,
                id="should raise error when cat age is not integer"
            ),
            pytest.param(
                5,
                "18",
                id="should raise error when dog age is not integer"
            ),
            pytest.param(
                "5",
                "18",
                id="should raise error when animals ages is not integer"
            ),
        ]
    )
    def test_raise_error_when_animals_ages_is_not_int(
            self,
            cat_age: Union[int, str],
            dog_age: Union[int, str]
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age=cat_age, dog_age=dog_age)

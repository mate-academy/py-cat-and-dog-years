import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,convert_to_human_age",
        [
            pytest.param(
                14, 14, [0, 0], id="0 <= ages < 15"
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
                100, 100, [21, 17], id="ages >= 29"
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

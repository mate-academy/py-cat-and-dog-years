import pytest
from app.main import get_human_age


class TestConvertAge:
    @pytest.mark.parametrize(
        "age_for_dog, age_for_cat, expected_age_dog_cat", [
            (-5, -5, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (28, 28, [3, 2]),
            (50, 50, [8, 7]),
            (100, 100, [21, 17]),
        ]
    )
    def test_dof_and_cat_age(
            self,
            age_for_dog: int,
            age_for_cat: int,
            expected_age_dog_cat: list[int]
    ) -> None:
        assert get_human_age(age_for_dog, age_for_cat) == expected_age_dog_cat

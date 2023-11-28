import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_ages",
        [
            pytest.param(
                14, 14, [0, 0], id="test converting first 14 into 0"
            ),
            pytest.param(
                23, 23, [1, 1], id="test converting first 15-23 into 1"
            ),
            pytest.param(
                100, 100, [21, 17], id="test converting age > 24"
            )
        ]
    )
    def test_convert_age_to_human(
            self,
            cat_age: int,
            dog_age: int,
            expected_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages

import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:

    @pytest.mark.parametrize(
        "cat_age, dog_age, value", [
            (14, 14, [0, 0]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3])
        ]
    )
    def human_age_tester(
            self,
            cat_age: int,
            dog_age: int,
            value: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == value

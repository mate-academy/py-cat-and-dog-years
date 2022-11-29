import pytest
from app.main import get_human_age


class TestGetAgeHuman:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                28,
                28,
                [3, 2],
                id="test function calculates age correctly"
            ),
            pytest.param(
                15,
                12,
                [1, 0],
                id="test function return 0 for animal which age "
                   "is less than human's year"
            ),
        ]
    )
    def test_function_calculations(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

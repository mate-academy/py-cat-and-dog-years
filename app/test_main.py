import pytest
from typing import Type
from app.main import get_human_age


class TestCheckResults:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            (14,
             14,
             [0, 0],
             ),
            (15,
             15,
             [1, 1],
             ),
            (23,
             23,
             [1, 1],
             ),
            (24,
             24,
             [2, 2],
             ),
            (27,
             28,
             [2, 2],
             ),
            (28,
             29,
             [3, 3],
             ),

        ]
    )
    def test_check_results(self,
                           cat_age: int,
                           dog_age: int,
                           human_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


class TestCheckErrors:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ("55",
             55,
             TypeError,
             ),
        ]
    )
    def test_raising_errors(self,
                            cat_age: int,
                            dog_age: int,
                            expected_error: Type[Exception]) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

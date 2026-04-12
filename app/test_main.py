from app.main import get_human_age
import pytest
from typing import Any


class TestGetHumanAgeDogArgument:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_list",
        [
            pytest.param(0, 0, [0, 0],
                         id="should return 0 if arguments "
                            "are 0"),
            pytest.param(14, 14, [0, 0],
                         id="should not increase first "
                            "year if arguments are 14"),
            pytest.param(15, 15, [1, 1],
                         id="should increase first "
                            "cat and dog human ages"),
            pytest.param(23, 23, [1, 1],
                         id="should not increase second "
                            "cat and dog human ages"),
            pytest.param(24, 24, [2, 2],
                         id="should increase second "
                            "cat and dog human ages"),
            pytest.param(27, 28, [2, 2],
                         id="should not increase third "
                            "cat and dog human ages"),
            pytest.param(28, 29, [3, 3],
                         id="should increase third "
                            "cat and dog human ages"),
            pytest.param(100, 100, [21, 17],
                         id="should return correct human ages"),
        ]
    )
    def test_should_return_right_logic_ages(self,
                                            cat_age: int,
                                            dog_age: int,
                                            expected_list: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(-1, 0, ValueError,
                         id="should return ValueError "
                            "if cat_age is less than 0"),
            pytest.param(14, -31, ValueError,
                         id="should return ValueError "
                            "if dog_age is less than 0"),
            pytest.param(1444, 31, ValueError,
                         id="should return ValueError "
                            "if cat_age is too large"),
            pytest.param(13, 1333, ValueError,
                         id="should return ValueError "
                            "if dog_age is too large"),
            pytest.param(13, "13", TypeError,
                         id="should return TypeError "
                            "if argument is str"),
            pytest.param([12], 12, TypeError,
                         id="should return TypeError "
                            "if argument is list"),
            pytest.param(13, {"age": 12}, TypeError,
                         id="should return TypeError "
                            "if argument is dict"),
        ]
    )
    def test_should_raising_error(self,
                                  cat_age: int,
                                  dog_age: int,
                                  expected_error: Any
                                  ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)

import pytest

from typing import Any
from app.main import get_human_age


class TestConvertingAges:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(0, 0, [0, 0], id="test zeroes"),
            pytest.param(14, 14, [0, 0], id="test value between 0 and 15"),
            pytest.param(15, 15, [1, 1], id="test 15 years"),
            pytest.param(24, 24, [2, 2], id="test 24 years (15 plus 9)"),
            pytest.param(28, 28, [3, 2],
                         id="test the difference after second human year"),
        ]
    )
    def test_human_age(self,
                       cat_age: int,
                       dog_age: int,
                       result: list) -> None:
        assert (get_human_age(cat_age, dog_age) == result
                ), (f"Converting of {cat_age} cat age and "
                    f"{dog_age} dog age should be equal to "
                    f"{result}")

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            pytest.param("0", "0", TypeError, id="test strings values"),
            pytest.param([10], [10], TypeError, id="test lists values"),
        ]
    )
    def test_are_values_correct(self,
                                cat_age: Any,
                                dog_age: Any,
                                error: type[TypeError]) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)

import pytest

from app.main import get_human_age

class TestForWorkingCases:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_to_get_correct_result(
            self,
            cat_age,
            dog_age, result
    ):
        assert get_human_age(cat_age, dog_age) == result


class TestForErrors:
    def test_incorrect_type(self):
        with pytest.raises(TypeError):
            get_human_age("28", "28")
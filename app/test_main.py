from app.main import get_human_age
import pytest


class Test:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (28, 28, [3, 2]),
            (11, 15, [0, 1]),
            (15, 10, [1, 0]),
            (-1, -12, [0, 0]),
            (340, 280, [81, 53])
        ]
    )
    def test_get_human_age(self,
                           cat_age,
                           dog_age,
                           result
                           ):
        assert get_human_age(cat_age, dog_age) == result

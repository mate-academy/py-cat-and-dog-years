import pytest

from app.main import get_human_age


class TestHumanAge:

    @pytest.mark.parametrize("cat_age, dog_age, human_age", [
        pytest.param(0,
                     0,
                     [0, 0],
                     id="Function should return [0, 0] if age equal 0"),
        pytest.param(14,
                     14,
                     [0, 0],
                     id="Function should round floor(down)"),
        pytest.param(15,
                     15,
                     [1, 1],
                     id="Function should count years"),
        pytest.param(28,
                     28,
                     [3, 2],
                     id="Function should return different ages"),
        pytest.param(100, 100, [21, 17],
                     id="Function should return [21, 17] if age equal 100")
    ])
    def test_human_age_function(self,
                                cat_age: int,
                                dog_age: int,
                                human_age: list
                                ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

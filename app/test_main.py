import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        pytest.param(0, 0, [0, 0],
                     id="Should return zeros, when initial data is zero"),
        pytest.param(14, 14, [0, 0],
                     id="Should return zeros, when ages are less than 15"),
        pytest.param(15, 23, [1, 1],
                     id="Should return 1 human year, "
                        "if age of the animal is 15 to 23 inclusive"),
        pytest.param(24, 24, [2, 2],
                     id="Should return 2 human years after age of 24"),
        pytest.param(28, 28, [3, 2],
                     id="Should add one more human year after age of 24 "
                        "every 4 year for cat and 5 for dog"),
        pytest.param(100, 100, [21, 17],
                     id="Should add extra human year after 28 every 4 year "
                        "for cat and after 29 every 5 year for dog")
    ])
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected

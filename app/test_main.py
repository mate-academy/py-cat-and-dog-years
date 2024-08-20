import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0, 0, [0, 0],
                id="0 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                12, 12, [0, 0],
                id="12 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                20, 22, [1, 1],
                id="20/22 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                26, 26, [2, 2],
                id="26 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                100, 100, [21, 17],
                id="100 cat/dog years should convert into 21/17 human age."
            ),
        ]
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

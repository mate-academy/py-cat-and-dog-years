import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(0, 0, [0, 0],
                         id="test 0 cat/dog years"),
            pytest.param(14, 14, [0, 0],
                         id="test under 15 cat/dog years"),
            pytest.param(15, 15, [1, 1],
                         id="test 15 cat/dog years"),
            pytest.param(23, 23, [1, 1],
                         id="test above 15 cat/dog years"),
            pytest.param(24, 24, [2, 2],
                         id="test every 9 cat/dog years"),
            pytest.param(27, 27, [2, 2],
                         id="test after 9 cat/dog years"),
            pytest.param(28, 28, [3, 2],
                         id="test every 4/5 cat/dog years"),
            pytest.param(100, 100, [21, 17],
                         id="test repeated 4/5 cat/dog years")
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


if __name__ == '__main__':
    pytest.main()

import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(0, 0, [0, 0], id="both ages are 0"),
            pytest.param(14, 14, [0, 0], id="both ages are 14"),
            pytest.param(23, 23, [1, 1], id="both ages are 23"),
            pytest.param(28, 28, [3, 2], id="both ages are 28"),
            pytest.param(32, 32, [4, 3], id="both ages are 32"),
            pytest.param(18, 18, [1, 1], id="both ages are 18"),
            pytest.param(100, 100, [21, 17], id="both ages are 100"),
        ]
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected: list
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected


if __name__ == "__main__":
    pytest.main()

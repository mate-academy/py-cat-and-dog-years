import pytest

from app.main import get_human_age


class TestHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(-1, -1, [0, 0]),
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(415, 510, [99, 99])
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            human_age: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age


class TestIncorrectDataType:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param("0", 0),
            pytest.param("0", "0"),
            pytest.param(None, 10)
        ]
    )
    def test_get_incorrect_data_type(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

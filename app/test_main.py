from app.main import get_human_age
import pytest


class TestAnimal:
    @pytest.mark.parametrize("cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (16, 0, [1, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]
    )
    def test_should_check_age_animal_is_human(self, cat_age: int, dog_age: int, expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    def test_should_raise_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 2.5)

    def test_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            get_human_age(-5, -5)

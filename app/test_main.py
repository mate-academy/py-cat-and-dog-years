from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat, dog, exp",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
class TestAnimals:
    def test_if_age_is_integer(
            self,
            cat: int,
            dog: int,
            exp: list) -> None:
        assert all(isinstance(num, int) for num in get_human_age(cat, dog))

    def test_if_age_is_positive(
            self,
            cat: int,
            dog: int,
            exp: list) -> None:
        assert all(num >= 0 for num in get_human_age(cat, dog))

    def test_cats_and_dogs_equivalent_age(
            self,
            cat: int,
            dog: int, exp: list) -> None:
        assert get_human_age(cat, dog) == exp


class TestEdgecases:
    def test_negative_cat_age(self) -> None:
        result = get_human_age(-1, 15)
        assert result[0] == 0
        assert result[1] == 1

    def test_negative_dog_age(self) -> None:
        result = get_human_age(15, -10)
        assert result[0] == 1
        assert result[1] == 0

    def test_both_negative_ages(self) -> None:
        result = get_human_age(-10, -10)
        assert result[0] == 0
        assert result[1] == 0

    def test_cat_age_string_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("a", 5)

    def test_dog_age_string_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(5, "a")

    def test_float_cat_age_string_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(15.7, 20)

    def test_float_dog_age_string_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(15, 20.5)

    def test_none_values_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(None, 20)

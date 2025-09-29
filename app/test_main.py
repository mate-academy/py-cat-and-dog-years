import pytest
from app.main import get_human_age


class TestBasicFunctionality:
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ])
    def test_examples(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestInputValidation:
    def test_invalid_types(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", 1)
        with pytest.raises(TypeError):
            get_human_age(1, "1")

    @pytest.mark.parametrize("cat_age, dog_age", [
        (-1, -1), (-100, 0), (0, -100), (-50, -50)
    ])
    def test_negative_ages(self, cat_age: int, dog_age: int) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]


class TestBoundaryValues:
    @pytest.mark.parametrize("cat_age, expected", [
        (15, 1), (24, 2), (28, 3), (32, 4)
    ])
    def test_cat_boundaries(self, cat_age: int, expected: int) -> None:
        assert get_human_age(cat_age, 0)[0] == expected

    @pytest.mark.parametrize("dog_age, expected", [
        (15, 1), (24, 2), (29, 3), (34, 4)
    ])
    def test_dog_boundaries(self, dog_age: int, expected: int) -> None:
        assert get_human_age(0, dog_age)[1] == expected

    @pytest.mark.parametrize("cat, dog, expected", [
        (28, 27, [3, 2]), (27, 29, [2, 3]), (32, 29, [4, 3])
    ])
    def test_independence(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

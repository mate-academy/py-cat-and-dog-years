import pytest
from typing import Any


from app.main import get_human_age


class TestAgeForAnimal:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_get_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-1, 5, [0, 0]),
            (5, -1, [0, 0]),
            (0, 5, [0, 0]),
            (5, 0, [0, 0]),
            (1000, 2000, [246, 397])
        ]
    )
    def test_edge_cases(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (5, 5),
            (2, 7),
        ]
    )
    def test_normal_cases(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (10, 10, [0, 0]),
            (19, 20, [1, 1]),
            (23, 25, [1, 2]),
        ]
    )
    def test_additional_cases(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestIntegerInput:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (5, 5),
            (2, 7)
        ]
    )
    def test_integer_inputs(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]


class TestErrorCases:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("A", 5),
            (10, [5, 6]),
            (True, 3)
        ]
    )
    def test_error_cases(
            self,
            cat_age: Any,
            dog_age: Any,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

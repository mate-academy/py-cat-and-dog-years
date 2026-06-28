from typing import Any

import pytest

from app import main


class TestGetHumanAge:

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
            (100, 100, [21, 17]),
        ],
    )
    def test_basic_examples(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:

        assert main.get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, expected_cat",
        [
            (0, 0),
            (1, 0),
            (14, 0),
            (15, 1),
            (16, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (28, 3),
            (31, 3),
            (32, 4),
            (50, 8),
        ],
    )
    def test_cat_age_boundaries(self, cat_age: int, expected_cat: int) -> None:
        result = main.get_human_age(cat_age, 0)
        assert result[0] == expected_cat
        assert result[1] == 0

    @pytest.mark.parametrize(
        "dog_age, expected_dog",
        [
            (0, 0),
            (1, 0),
            (14, 0),
            (15, 1),
            (16, 1),
            (23, 1),
            (24, 2),
            (28, 2),
            (29, 3),
            (33, 3),
            (34, 4),
            (50, 7),
        ],
    )
    def test_dog_age_boundaries(self, dog_age: int, expected_dog: int) -> None:
        result = main.get_human_age(0, dog_age)
        assert result[0] == 0
        assert result[1] == expected_dog

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (100, 0, [21, 0]),
            (0, 100, [0, 17]),
            (15, 100, [1, 17]),
            (100, 15, [21, 1]),
        ],
    )
    def test_independence_of_calculations(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:

        assert main.get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (-1, 0, [0, 0]),
            (0, -1, [0, 0]),
            (-5, -5, [0, 0]),
            (-100, 100, [0, 17]),
            (100, -100, [21, 0]),
        ],
    )
    def test_negative_ages(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:

        assert main.get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("15", 15),
            (15, "15"),
            (None, 15),
            (15, None),
            ([15], 15),
            (15, {"age": 15}),
            (15.5, 15),
            (15, 15.5),
        ],
    )
    def test_invalid_types_raise_type_error(
        self, cat_age: Any, dog_age: Any
    ) -> None:

        with pytest.raises(TypeError):
            main.get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (1000, 1000, [246, 197]),
            (10000, 10000, [2496, 1997]),
        ],
    )
    def test_large_numbers(
        self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert main.get_human_age(cat_age, dog_age) == expected

    # Перевірка структури результату
    def test_return_type_is_list(self) -> None:
        result = main.get_human_age(10, 10)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_result_elements_are_integers(self) -> None:
        result = main.get_human_age(27, 27)
        assert all(isinstance(x, int) for x in result)

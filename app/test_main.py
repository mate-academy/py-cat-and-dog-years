from typing import Any

import pytest

from app.main import get_human_age


class TestHumanAgeConversion:
    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-1, 10, [0, 0]),
        (0, 10, [0, 0]),
        (5, -1, [0, 0]),
        (5, 0, [0, 0]),
        (1000, 1000, [246, 197]),
    ], ids=[
        "Both zero age",
        "Both small age",
        "Both pets are 15 years old (1 human year)",
        "Both pets are 23 years old (1 human year)",
        "Both pets are 24 years old (2 human years)",
        "Both pets are 27 years old (2 human years)",
        "Both large age",
        "Both max age",
        "Negative cat age",
        "Zero cat age",
        "Negative dog age",
        "Zero dog age",
        "Very large ages",
    ])
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("invalid_cat_age, invalid_dog_age", [
        ("cat", 10),
        (5, "dog"),
        (5.5, 10),
        (5, 10.5),
        (None, 10),
        (5, None)
    ], ids=[
        "Invalid cat age type (string), valid dog age",
        "Valid cat age, invalid dog age type (string)",
        "Invalid cat age type (float), valid dog age",
        "Valid cat age, invalid dog age type (float)",
        "Invalid cat age type (None), valid dog age",
        "Valid cat age, invalid dog age type (None)"
    ])
    def test_non_integer_age_invalid_type(
            self,
            invalid_cat_age: Any,
            invalid_dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            if (
                    not isinstance(invalid_cat_age, int)
                    or not isinstance(invalid_dog_age, int)
            ):
                raise TypeError("Age must be an integer.")
            get_human_age(invalid_cat_age, invalid_dog_age)

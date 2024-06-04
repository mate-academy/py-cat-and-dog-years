import pytest
from app.main import get_human_age


class TestConvertHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(14, 14, [0, 0],
                         id="14_cat_dog"),
            pytest.param(15, 15, [1, 1],
                         id="15_cat_dog"),
            pytest.param(23, 23, [1, 1],
                         id="23_cat_dog"),
            pytest.param(24, 24, [2, 2],
                         id="24_cat_dog"),
            pytest.param(27, 28, [2, 2],
                         id="27_28_cat_dog"),
            pytest.param(29, 28, [3, 2],
                         id="28_29_cat_dog"),
            pytest.param(-1, -1, [0, 0],
                         id="negative_years"),
            pytest.param(1000, 1000, [246, 197],
                         id="1000_years"),
            pytest.param(1500, 2000, [371, 397],
                         id="1500_2000_years")
        ]
    )
    def test_convert_human_age(self,
                               cat_age: int,
                               dog_age: int,
                               expected: list
                               ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected, (
            f"For {cat_age} cat years and "
            f"{dog_age} dog years, expected {expected} "
            f"but got {result}"
        )


class TestInvalidInputType:
    @pytest.mark.parametrize("cat_age, dog_age", [
        ("string", 10),
        (10, "string"),
        ("string", "string"),
        (None, 10),
        (10, None),
        (None, None),
        ([10], 10),
        (10, [10]),
        ([10], [10])
    ])
    def test_invalid_input_type(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

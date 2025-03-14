import pytest

from app.main import get_human_age

class TestGetAge:
    @pytest.mark.parametrize("cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_raising_error(
            self,
            cat_age,
            dog_age,
            expected
    ):
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "invalid_cat, invalid_dog",
        [
            ("abc", 10),
            (10, "xyz"),
            (None, 10),
            (10, None),
            ([], {}),
        ]
    )
    def test_raise_error_negative_value(
            self,
            invalid_cat,
            invalid_dog
    ):
        with pytest.raises(TypeError):
            get_human_age(invalid_cat, invalid_dog)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (10000, 10000),
        ]
    )
    def test_very_big_value(
            self,
            cat_age,
            dog_age
    ):
        result = get_human_age(cat_age, dog_age)
        assert result[0] > 0 and result[1] > 0